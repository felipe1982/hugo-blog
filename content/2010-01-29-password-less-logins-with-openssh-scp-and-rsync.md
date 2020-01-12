---
title: Password-less Logins with OpenSSH, scp, and rsync
author: felipe
type: post
date: 2010-01-29T07:39:31+00:00
url: /password-less-logins-with-openssh-scp-and-rsync/
categories:
  - computers
  - GNU Linux
  - security
  - software
  - technology

---
**UPDATE**: I changed &#8216;>&#8217; (erase file, then write to file) to &#8216;>>&#8217; (append to file). This avoids you overwriting your, or other peoples&#8217;, public keys.

Setting up password-less logins is both dangerous, and mighty. It allows one to authenticate to an OpenSSH server without typing in a password. Authentication is gained via knowledge of a private key.

#### Generate a Public/Private Key Pair

<pre>$&gt; ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/felipe/.ssh/id_rsa):
Enter passphrase (empty for no passphrase): <strong>&lt;ENTER&gt;</strong>
Enter same passphrase again: <strong>&lt;ENTER&gt;</strong>
Your identification has been saved in /home/felipe/.ssh/id_rsa.
Your public key has been saved in /home/felipe/.ssh/id_rsa.pub.
The key fingerprint is:
d7:79:c3:01:ce:90:71:a2:a2:3d:83:26:fb:9a:1f:5b felipe@linux.local</pre>

You will then find two files inside your directory. Keep them safe, secure, and secret. The public key (the one with **.pub** at the end) can be widely disemmindated. It represents the antonym of secrecy and privacy. The **_private_** key, however, must remain private and secret _at all times_.

#### Copy the PUBLIC key to a remote OpenSSH server

You must copy your _public_ key to a remote host. The host will verify that you own the _private_ key by encrypting a _&#8220;challenge&#8221;_ and forcing your ssh client to decrypt it. If successful, you are authenticated, and admitted entrance. A password isn&#8217;t required.

<pre>$&gt; cat /home/felipe/.ssh/id_rsa.pub | ssh felipe@remote-host.com \
"cat - &gt;&gt; .ssh/authorized_keys"
felipe@remote-host.com's password: <strong>&lt;PASSWORD&gt;</strong></pre>

This copies your _public_ key the _authorized_keys_ file (NB: authorized_keys2 is deprecated and no longer recommended for use. OpenSSH checks both).

#### Testing Phase

&#8216;logout&#8217; or &#8216;exit&#8217; and try:

<pre>$&gt; ssh felipe@remote-host.com</pre>

It should _not_ ask you for a password. You should automatically be logged into the remote system.

#### Works with scp and rsync too!

&#8216;scp&#8217; and &#8216;rsync&#8217; both use a ssh client at the backend, and so will also authenticate automatically utilising your public and private key pair. Try:

<pre>$&gt; scp file_a felipe@remote-host.com:file_b</pre>

This should transfer without pausing to ask for your password. Likewise try:

<pre>$&gt; rsync -r /backups/2010/Jan felipe@remote-host.com:/backups/2010</pre>

This should backup your entire directory to remote-host.com without pausing to ask for a password. You can put a line similar to this one in a shell script, and run it with cron once a week or so. It will automatically backup your system, using OpenSSH, and proven secure and safe method for authentication of human and machines across an untrusted public network, away from curious eyes.