---
title: Fixing partition table in linux with sfdisk
author: felipe
type: post
date: 2012-02-15T00:11:53+00:00
url: /fixing-partition-table-in-linux-with-sfdisk/
categories:
  - computers
  - GNU Linux
  - software
tags:
  - extended partition
  - linux
  - logical partition
  - partitioning
  - partitions
  - sfdisk

---
Manipulating partition tables on MS-DOS labelled hard disk (the most common type as of this writing) is an extemely important skill to have as a System Administrator. If one or more partitions gets deleted or modified in an unintentional way, it is imperative that one know how to restore or modify the partitions to rectify the problem.

<!--more-->I was trying to increase the size of one of my ext3 partitions on RHEL. Following the instructions, I deleted the logical partition, and its parent extended partition.

I wrote down the beginning and ending sectors of both partitions

`/dev/sda4 start: 29559600 end: 167772159<br />
/dev/sda5 start: 29550663 end: 167772159`

Note that the logical partition begins 63s after the extended partition (presumably for the Extended Boot Record).

Unfortunately I didn&#8217;t make a backup prior to fvcking up my partition table.

When I was trying to make a larger extended partition, and subsequently a larger logical partition, the logical partition wasn&#8217;t starting at the same point. e2fsck was complaining that it the partition wasn&#8217;t a valid ext2/3 partition.

I had to re-create the partitions with the same starting sector. But fdisk and parted both weren&#8217;t able to do the job that I asked (I was using [partedmagic liveCD][1]). I had heard of sfdisk, but had never before used it! I was scared!

First, I wanted to make a backup of my partition table (now I learned my lesson)!

`sfdisk /dev/sda -d > sda-patition-table.txt`

The following can restore the drive to the way it was:

`sfdisk /dev/sda < sda-partition-table.txt`

Make copy of the partition table:

`cp sda-patition-table.txt mygoals.txt`

Edit the file to make the changes you need:

`vi mygoals.txt`

\# partition table of /dev/sda
  
unit: sectors

/dev/sda1 : start=       63, size=   208782, Id=83, bootable
  
/dev/sda2 : start=   208845, size= 20964825, Id=83
  
/dev/sda3 : start= 21173670, size=  8385930, Id=82
  
/dev/sda4 : start= 29559600, size=507311312, Id= f
  
/dev/sda5 : start= 29559663, size=507311249, Id=83

Above are _post-changes_ so you aren&#8217;t able to view what my table _used_ to look like. As you can see, I&#8217;ve recreated the starting sectors of partition 4 and 5, and extended them to their maximum size (just use a simple calculator to determine partition sizes)

Run a test:

`sfdisk -n /dev/sda -O change1.txt < mygoals.txt`

-n does a dry run (nothing will be saved to disk)
  
-O saves binary partition table data to file change1.txt
  
mygoals.txt are the instructions given to sfdisk

When you are happy with the output, make the changes permanent:

`sfdisk --force /dev/sda -O change2.txt < mygoals.txt`

Finally, run a filesystem check:

`e2fsck -f -v /dev/sda5`

 [1]: http://partedmagic.com