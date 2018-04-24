---
title: Logging to a remote Linux syslog server
author: felipe
type: post
date: 2012-02-20T06:12:20+00:00
url: /logging-to-a-remote-linux-syslog-server/
categories:
  - GNU Linux

---
If you have every experienced the difficulty in not being able to read your log files, either because the hard drives have crashed, or the OS cannot be started, or your machine has been compromised, you may benefit from logging to a remote server. <!--more-->

To set up remote logging, you must make a single modification to the server. I&#8217;m speaking from RHEL 5, you may be using Debian, Ubuntu, or CentOS, or some other distribution. You may need to find more information about those distributions before continuing.

To begin, you must edit **/etc/sysconfig/syslog**, and change this line from:

> SYSLOGD_OPTIONS=&#8221;-m 0&#8243;

And modify the line to:

> SYSLOGD_OPTIONS=&#8221;-x -r -m 0&#8243;

**-x** disabled reverse DNS lookups, saving bandwidth, configuration hassles, and time

**-r** enabled listening to logs from other servers

On each client machine, you must edit **/etc/syslog.conf** and modify the _last_ line to read something like:

> mail.none;*.info        @syslog.example.com

syslog.example.com is the hostname, or ip address, of your remote logging server.

Restart both the server and client syslog daemons. From the client machine, run a test, similar to:

> logger test 1 from client1.example.com

And on the server run:

> tail /var/log/messages

Thanks to [Enable remote logging with syslog][1]

 [1]: http://www.techrepublic.com/article/tech-tip-enable-remote-logging-with-syslog/5285872