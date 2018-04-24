---
title: Easy symmetrical blowfish encryption with VIM
author: felipe
type: post
date: 2011-04-04T10:52:09+00:00
url: /easy-symmetrical-blowfish-encryption-with-vim/
categories:
  - security

---
Just run:

    vim -x filename

And vim will automatically encrypt your file upon saving it. I&#8217;m still not sure how it treats the .swp file it creates upon editing a file.

If you forgot the -x switch, you can still encrypt your file by typing

    ESC

then,

    :X (colon and capital x)