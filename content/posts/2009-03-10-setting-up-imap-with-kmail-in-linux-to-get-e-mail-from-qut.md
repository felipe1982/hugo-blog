---
title: Setting up IMAP with KMail in Linux to get e-mail from QUT
author: felipe
type: post
date: 2009-03-10T11:46:14+00:00
url: /setting-up-imap-with-kmail-in-linux-to-get-e-mail-from-qut/
categories:
  - computers
  - security
tags:
  - imap
  - kmail
  - qut
  - vpnc

---
These instructions are for QUT students. I do not know if they will work for QUT staff. Use at your own risk.

You need &#8216;vpnc&#8217; program (install it with your pkg mgr). Then download [off-campus.conf][1] file and save it to _/etc/vpnc/_ directory. You could name it _default.conf_ if it will be your only vpnc connection. The contents should begin with at least:

<pre>IPSec gateway sas.qut.edu.au
IPSec ID qut
IPSec secret qutaccess</pre>

As root run _vpnc off-campus_ of just _vpnc_ if you renamed it to _default.conf_. Enter username/password when prompted.

In Kmail, you setup IMAP connection using SSL, username/password and port 993 to host _mail.qut.edu.au_. SMTP uses NO ecryption, but authentication method is LOGIN (not PLAIN) and port 25 on host _mail.qut.edu.au_.

To exit vpnc type _vpnc-disconnect_ as root.

I hope this helps someone.

_References__
  
<http://www.its.qut.edu.au/offcampusaccess/sas/linux.jsp>
  
_

 [1]: https://www.qut.edu.au/its/downloads/sas/off-campus.conf