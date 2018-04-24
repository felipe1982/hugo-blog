---
title: Amarok cannot connect to MySQL database
author: felipe
type: post
date: 2010-11-25T04:22:49+00:00
url: /amarok-cannot-connect-to-mysql-database/
categories:
  - computers
  - GNU Linux
tags:
  - amarok
  - linux
  - mysql

---
I deleted all instances of &#8216;amarok&#8217; in `$HOME/.kde4/share`, and dropped the &#8216;amarokdb&#8217; database, and dropped &#8216;amarokuser&#8217;, and re-created everything, but it still wouldn&#8217;t connect.

It turns out the solution is simple. Just change the password in the Amarok settings page from &#8216;password&#8217; to something else (e.g. &#8216;password123&#8217;). Change the &#8216;amarokuser&#8217; password, too, in mysql. Restart Amarok, and they can connect.

This is a bug in Amarok, as it doesn&#8217;t have a default password configured, one must be explicitly set.  [Source][1]

 [1]: http://forum.kde.org/viewtopic.php?f=115&t=89052