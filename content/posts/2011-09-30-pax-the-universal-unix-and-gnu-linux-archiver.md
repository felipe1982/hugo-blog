---
title: 'PAX: the universal UNIX and GNU Linux archiver'
author: felipe
type: post
date: 2011-09-30T06:20:21+00:00
url: /pax-the-universal-unix-and-gnu-linux-archiver/
categories:
  - GNU Linux
tags:
  - cpio
  - pax
  - tar

---
pax, which means _peace_ in Latin, combines the best of both cpio and tar, which are found in nearly all modern GNU/Linux distributions. However, it _appears_ as though it hasn&#8217;t been updated in several _years!_

Benefits include:

  * can use &#8216;find&#8217; to get list of files, which is then piped through to pax (cpio style)
  * can read and write many archive formats, including ustar (default), cpio, and many others
  * can do copy-pass mode (copy entire directory tree to another location)
  * can do gzip compression on the fly (tar style)

man pax will show you more example