---
title: User your own timezone in Linux shell
author: felipe
type: post
date: 2012-11-28T05:59:49+00:00
url: /user-your-own-timezone-in-linux-shell/
tc-thumb-fld:
  - 'a:2:{s:9:"_thumb_id";b:0;s:11:"_thumb_type";s:10:"attachment";}'
categories:
  - GNU Linux
tags:
  - date
  - time
  - timezone
  - webhost

---
Do you use a hosting provider that has a different timezone than you do? You can change the appearance of the timezone easily, without root access, or playing around with dates and times.

You can use the <tt>tzselect</tt> command. It will ask you for your Continent, your State/Province, and will output the command you need to modify your timezone.

I live in Brisbane, Australia, so my timezone is **Australia/Brisbane**. All I needed to do what append one line to my <tt>.bash_profile</tt>

> echo &#8220;export TZ=Australia/Brisbane&#8221; >> .bash_profile

Now <tt>date</tt> returns the correct date and time, and all my files have local timestamps.