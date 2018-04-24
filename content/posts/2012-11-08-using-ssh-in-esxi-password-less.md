---
title: Using SSH in ESXi (Password-Less)
author: felipe
type: post
date: 2012-11-08T04:57:23+00:00
url: /using-ssh-in-esxi-password-less/
tc-thumb-fld:
  - 'a:2:{s:9:"_thumb_id";b:0;s:11:"_thumb_type";s:10:"attachment";}'
categories:
  - GNU Linux
  - security
tags:
  - dropbear
  - esxi
  - public key
  - ssh
  - vmware

---
We can now setup Public Key Authentication and Use SSH to connect from ESXi to another (Linux) computer system  using openSSHD (SSH Daemon).

<pre>cat ~/.ssh/id.dsa.pub | ssh root@esxi ‘cat - &gt;&gt; /etc/ssh/keys-root/authorized_keys’</pre>