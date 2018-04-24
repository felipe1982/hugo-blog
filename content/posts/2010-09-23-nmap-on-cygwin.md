---
title: Nmap on Cygwin
author: felipe
type: post
date: 2010-09-23T04:17:16+00:00
url: /nmap-on-cygwin/
categories:
  - computers
  - security
  - software
tags:
  - cygwin
  - nmap
  - port scan

---
Installed nmap on cygwin. Dead easy!

  1. Download and install [Cygwin][1]
  2. Download and install [WinPCAP][2]
  3. Accept most defaults
  4. Do the default installation, typically C:\cygwin\
  5. [Download nmap for windows (zip)][3]
  6. Open the zip file
  7. Double click the folder inside the zip, a large list of files should appear
  8. Extract these files (and not the folder which contains them) to C:\cygwin\usr\local\bin
  9. Open cygwin
 10. Type 
      * `nmap --version`
 11. Your nmap installation on cygwin is now complete

**Update 3/May/2012:** Try running the vcredist_x86.exe file found in the zip archive if nmap doesn&#8217;t seem to run.

For a general understanding of nmap, just type nmap. For a more detailed comprehension, [read the manual][4], and [search the web][5].

 [1]: http://cygwin.org
 [2]: http://www.winpcap.org/install/default.htm
 [3]: http://nmap.org/download.html#windows
 [4]: http://nmap.org/book/man.html
 [5]: http://google.com