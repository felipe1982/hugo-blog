---
title: Installing and configuring BOINC on openSUSE
author: felipe
type: post
date: 2012-02-10T17:30:22+00:00
url: /installing-and-configuring-boinc-on-opensuse/
categories:
  - GNU Linux
  - software
tags:
  - boinc
  - CPU
  - GPU
  - opensuse
  - seti

---
I tried installing and configuring BOINC on openSUSE but found some struggles along the way. I think I&#8217;ve got it set up and working, although we won&#8217;t see any evidence of problems until it has been running for several days.
  
<!--more-->


  
After installing boinc-client and boinc-manager from zypper, there is something very important that needs to be changed to the RC script (/etc/init.d/boinc-client) will actually work!

## Boinc Client

openSUSE creates a user and a group both named boinc, but the user&#8217;s shell is /sbin/nologin, which doesn&#8217;t help, because the rc script uses su to execute the boinc-client as the user boinc, but it can&#8217;t because it has no shell! This gives it the Bash shell:

<p style="padding-left: 30px;">
  # usermod -s /bin/bash boinc
</p>

## Boinc Manager

Normally, the boinc manager needs to be manually connected to the daemon (boinc-client). But we can fix this, so that the boinc manager connects to the daemon instance upon launching.

Check your current groups

<pre style="padding-left: 30px;">id $USER</pre>

Now add yourself to the boinc group (boinc group _**must**_ be present). <span style="text-decoration: underline;">The values for -g and for -G should match the output from above</span>! But now you&#8217;re adding <span style="text-decoration: underline;">boinc</span>.

<pre style="padding-left: 30px;">usermod -g users -G audio,video,floppy,boinc $USER</pre>

Now edit some directory permissions to let you write into the boinc working directory (/var/lib/boinc). This directory was automatically created when boinc was installed.

<pre style="padding-left: 30px;">chmod g+rwX /var/lib/boinc
ln -s /var/lib/boinc/gui_rpc_auth.cfg ~/</pre>

There is one more command that I have not yet tried, and things _**do seem to work without it**_.

chmod g+rw /var/lib/boinc/*

## sysconfig

By default, the LOCKFILE is set to be /var/lock/subsys/boinc-client, which is very stupid, since ../subsys directory does not exist on a stock openSUSE 12.1 system! I changed it to be /var/run/${BOINCEXE_NAME}.lock (which is included as one of the comments)

## Thanks

Thanks to [https://boinc.berkeley.edu/wiki/Installing\_BOINC\_on_Fedora][1] for helping me solve the boinc-manager problem.

&nbsp;

 [1]: https://boinc.berkeley.edu/wiki/Installing_BOINC_on_Fedora