---
title: GNU find and -perm option – Part 1
author: felipe
type: post
date: 2010-06-06T01:27:58+00:00
url: /gnu-find-and-perm-option/
categories:
  - GNU Linux

---
I have always found GNU `find` to be a little bit tricky to use. It is indeed quite a powerful program. It allows you to search anywhere, for anything! With the output, you can use the -exec option to run a command on each and every file find finds.

<!--more-->

-perm is a fantastic feature to GNU find. With it, you can search for file permissions. Lately, I&#8217;ve been running it to find out which files have _at least_ the SETUID bit set.

> [setuid and setgid][1] (short for set user ID upon execution and set group ID upon execution, respectively) are Unix access rights flags that allow users to run an executable with the permissions of the executable&#8217;s owner or group. They are often used to allow users on a computer system to run programs with temporarily elevated privileges in order to perform a specific task.

To search for files that have _at least_ the SETUID (4xxx), _or_ SETGID (2xxx), _or_ sticky bits (1xxx) set, you run:

<pre>find /directory -perm /7000</pre>

This will make find search for files that have at least one of the bits turned on that make up the octal value &#8216;7.&#8217; 7 is composed of 4+2+1, so it will search for files that have a 1, 2, 3, 4, 5, 6, or 7 as their first number.

  * 1xxx
  * 2xxx
  * 3xxx
  * 4xxx
  * 5xxx
  * 6xxx
  * 7xxx

_x_ here means any bit, or lack of a bit, such as 4640, or 5222.

Additionally,

<pre>find /directory -perm /222</pre>

searches for files that are writeable by someone. That is, it has _at least_ the &#8216;w&#8217; set for the user, _or_ the group, _or_ others, regardless if other bits that might be set, such as the e&#8217;x&#8217;ecute bit.

`find` has two other -perm features. We&#8217;ll talk about those next time.

 [1]: http://en.wikipedia.org/wiki/Setuid