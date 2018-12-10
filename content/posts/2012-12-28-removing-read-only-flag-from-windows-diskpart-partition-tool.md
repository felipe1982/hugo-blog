---
title: Removing read only flag from Windows Diskpart Partition tool
author: felipe
type: post
date: 2012-12-28T02:09:32+00:00
url: /removing-read-only-flag-from-windows-diskpart-partition-tool/
tc-thumb-fld:
  - 'a:2:{s:9:"_thumb_id";b:0;s:11:"_thumb_type";s:10:"attachment";}'
categories:
  - Australia
  - computers
tags:
  - diskpart
  - partition
  - windows

---
I was trying to investigate a failed disk from a RAID array using a USB hard drive dock and Windows 7. The problem was Windows was reporting that the disk was read-only, so it wouldn&#8217;t repartition the hard disk.

I opened up diskpart tool in windows (Run As Administrator) and tried to run the **clean** command, but again it complained that the hard drive was in read-only mode.

Finally, I found the way to remove the read-only flag, so I could <s>wipe the drive, and</s> scan it for bad sectors.

`<br />
DISKPART> list disk<br />
DISKPART> select disk 2<br />
DISKPART> list part<br />
DISKPART> select part 2<br />
DISKPART> attrib part clear readonly<br />
`