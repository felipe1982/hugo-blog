---
title: UTF-8 characters in FreeNAS with rsync and cygwin and Windows
author: felipe
type: post
date: 2009-11-27T18:56:17+00:00
url: /utf-8-characters-in-freenas-with-rsync-and-cygwin-and-windows/
categories:
  - computers

---
I&#8217;ve been having some problems with charsets (character sets) when using FreeNAS, rsync, deltacopy, and cygwin.

The filenames on a Windows box are either in UTF-8 or ISO-8859-1 (Latin1). The FreeNAS uses rsync to backup the files on the windows box, and saves them to a RAID array. I wasn&#8217;t sure if it was rsync, or FreeNAS causing the problem, but all characters with more than 7 significant bits (8 or more) were being &#8220;escaped&#8221; such as **\#303** instead of **Ñ**.

I found the solution by using the &#8220;-8&#8221; flag in rsync. Also, I overwrote the cygwin.dll file supplied by DeltaCopy with a [UTF-8-modified cygwin.dll][1], restarted DeltaCopy, and the filenames appeared correctly _and_ in UTF-8 (instead of ISO8859-1).

As always, remember to BACKUP before journeying on with this! Good Luck!

 [1]: http://www.okisoft.co.jp/esc/utf8-cygwin/