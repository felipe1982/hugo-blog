---
title: Largest File size on a DVD
author: felipe
type: post
date: 2012-05-09T06:05:55+00:00
url: /largest-file-size-on-a-dvd/
categories:
  - GNU Linux
  - technology
tags:
  - bytes
  - dvd
  - file size
  - split

---
The largest file size on a DVD is 4294967295 bytes. You can use this with GNU split, for example:

<pre>split --bytes 4294967295 file file_suffix_</pre>