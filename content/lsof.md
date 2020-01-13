---
title: List open files - lsof
author: felipe
type: post
date: 2019-12-17T15:51:19+10:00
url: /lsof-list-open-files/
categories:
  - linux
  - shell
---
`lsof` allows you to show what processes are using files on your system.

Some options of note:

- `+D` recursive directory
- `-x` traverse mount points and follow symbolic links
- `-p` process ID
- `-n` do not resolve hostnames
- `-P` do not resolve port names
- `-i` internet
  - `-i tcp`
  - `-i :80`
  - `-i tcp:80`
- `-F?` fields

