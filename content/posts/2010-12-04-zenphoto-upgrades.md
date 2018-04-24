---
title: zenphoto upgrades
author: felipe
type: post
date: 2010-12-04T01:18:25+00:00
url: /zenphoto-upgrades/
categories:
  - computers

---
I was initially having some issues doing an upgrade. It was, as it always seems to be, because I did not [RTFM][1].

  * Backup your MySQL database.
  * Backup customised themes or plugins or any other files
  * **_Delete_** the following files and folders: 
      * The zp-core folder
      * The themes that were distributed with Zenphoto
      * The files in the home dir (index.php, rss.php, sitemap.php etc.) that came with the distribution
  * Download the latest version and upload it to your server. **_Do not replace your albums or cache folder!_**
  * Make sure the .htaccess file is writeable. (If you do not have a .htaccess file, you will be given the opportunity to create one during setup.)
  * Move robots.txt
  * Visit www.example.org/zenphoto/ to start the automated setup wizard.
  * If it does not automatically start, visit www.example.org/zenphoto/zp-core/setup.php
  * Make sure everything checks out, and click go!
  * Follow the instructions.
  * You’re done! Enjoy.

 [1]: http://www.zenphoto.org/2008/08/installation-and-upgrading/#1