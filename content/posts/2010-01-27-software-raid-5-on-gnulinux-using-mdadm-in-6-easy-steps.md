---
title: Software RAID-5 on GNU/Linux Using mdadm In 6 Easy Steps
author: felipe
type: post
date: 2010-01-27T05:23:56+00:00
url: /software-raid-5-on-gnulinux-using-mdadm-in-6-easy-steps/
categories:
  - GNU Linux

---
For this setup, I used **4** 320GB sata 300 hard drives. This array is _not_ configured for booting, just for redundant storage. My four drives are:

  * sdb
  * sdc
  * sdd
  * sde

#### 1.  Ensure all partitions on the drives are erased

There are a few ways to do this. I just overwrite the first million bytes with <tt>zero</tt>es.

<pre>$&gt; dd if=/dev/urandom of=/dev/sdb bs=1M count=1</pre>

Another way to do it, is using fdisk, like this

<pre>$&gt; fdisk /dev/sdc
d (deletes a partition by its number)
1 (partition number)
w (writes changes to the disk)
q (quit without saving)</pre>

For best results, one should remove all partitions from all the RAID members.

#### 2.  After all partitions have been erased from all members, we must create RAID partitions.

We can use fdisk again, like this:

<pre>$&gt; fdisk /dev/sdd
n (this makes new partition)
p (primary (not extended))
1 (number 1)
start: &lt;press enter&gt;
end: &lt;press enter&gt;
t (selects partition type)
fd (0xFD is the symbol for Linux RAID partition)
w (writes changes to disk)
q (quits without saving changes)</pre>

Repeat this process for all your RAID members. **_Do not format these disks_**. We will first build the array, then format the array.

#### 3.  Tell mdadm to create an array with 4 members

<pre>$&gt; mdadm --create --level=5 --metadata=1.2 --raid-devices=4 \
 /dev/md0 /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1</pre>

  * **creates** the array from available members
  * select the raid **level** (we want RAID5, but 0, 1, 10, 5, 6 are available)
  * **metadata** ensures we have the most robust and up-to-date RAID system
  * **raid-devices** select 4 devices for our array. We could have done 3 devices, and one spare. A spare will automatically rebuild if any live members fail or die.
  * **/dev/md0** is the array
  * **sdb**, **sdc**, **sdd**, **sde** are the partitions that will be a part of this array

Now that you&#8217;ve created it,  you don&#8217;t need to assemble it. In case you need to, however, this is how you can do it.

<pre>$&gt; mdadm --assemble &lt;ARRAY&gt; &lt;DEVICES&gt; ...</pre>

<pre>$&gt; mdadm --assemble /dev/md0 /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1</pre>

#### 4.  mdadm is now creating and initialising the drives.

You can check progress with

<pre>$&gt; cat /proc/mdstat</pre>

It is a good practice to check your array every now and again. See a detailed report with:

<pre>$&gt; mdadm -vD /dev/md0</pre>

Which does a &#8211;verbose &#8211;detail &#8216;ed check of your array /dev/md0.

#### 5.  Partition and Format the Array

You can partition the array with your favourite program. Don&#8217;t partition the drives! Partition the array /dev/md0! I use fdisk:

<pre>$&gt; fdisk /dev/md0
n (new partition)
1 (number)
start: &lt;press enter&gt;
end: &lt;press enter&gt;
w (write changes to disk)
q (quit without saving changes)</pre>

Next you format the partition with your favourite filesystem. I like ext3. My distribution ships with a shortcut program called mkfs.ext3. You may require mke2fs, which by default create an ext2 filesystem. Add option -j to create a journaling ext3 filesystem. Type man mke2fs for more information.

<pre>$&gt; mkfs.ext3 -v -L ADD-A-LABEL /dev/md0p1</pre>

Where &#8216;p1&#8217; is the first partition on the array. The array may still show &#8216;rebuilding&#8217; bur it is usable. It will not be fully redundant, however, until rebuilding status shows 100%.

#### 6.  Create or Edit /etc/mdadm/mdadm.conf and /etc/fstab

It should read something like this:

<pre>#/etc/mdadm/mdadm.conf
DEVICE /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1
CREATE owner=root group=disk mode=0660 auto=yes
MAILADDR root
#MAILADDR xxxxx@domain.com
ARRAY /dev/md0 metadata=1.2 num-devices=4 devices=/dev/sdb1,/dev/sdc1,/dev/sdd1,/dev/sde1</pre>

Your /etc/fstab should include a line similar to:

<pre>#/etc/fstab
# automount /dev/md0 raid partition
/dev/md0p1  /mnt/mountpoint  ext3  rw,user  0 0</pre>

My /etc/fstab reads:

<pre>/dev/md0p1 /media/leopard ext3 rw,user,noacl,noatime,nodiratime,noauto 0 2</pre>

noacl,nodiratime,noatime should improve performance of ext3. noauto prevents filesystem from being mounted automatically, just in case (I&#8217;m paranoid). The &#8216;2&#8217; at the end makes fsck scan the drive after 31 or so mounts. See man mount for more options.

Update: There is another [terrific guide explaining how to modify and grow][1] a RAID1 array with 2 (or more) disks to a RAID5 array.

 [1]: http://www.n8gray.org/blog/2006/09/05/stupid-raid-tricks-with-evms-and-mdadm/