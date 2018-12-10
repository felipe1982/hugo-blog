---
title: aircrack-NG Intel PRO Wireless 3945 a/b/g SUPPORT!
author: felipe
type: post
date: 2010-11-04T07:57:17+00:00
url: /aircrack-ng-intel-pro-wireless-3945-abg-support/
categories:
  - security
tags:
  - aircrack
  - intel
  - WEP
  - wireless

---
Iwl3945 is the new driver for the Intel PRO/Wireless 3945ABG wireless chipset. It includes new features like:

  * Managed and monitor mode support in one driver
  * Enhanced injection support
  * Multiple interfaces on one device &#8211; use the aircrack suite on a monitor interface while remaining associated on a managed interface
  * Full radiotap support, for both incoming and outgoing packets
  * No more binary regulatory daemon needed, regulatory enforcement is done by the firmware

The driver is based on the [mac80211][1] stack, so the usual requirements apply (aircrack-ng 1.0-rc1, a recent version of libnl, a fairly new kernel, etc.)

I&#8217;m quite excited about this, because previously my chip wasn&#8217;t able to do packet injection. Now, I can force WEP client to dissassociate from their WAPs, and I can potentially break WEP! My Core2Duo 1.8GHz machine may not have the horsepower, but my AMD 6400+ X2 can certainly handle it.

[Aircrack-NG and Intel iwl3945 Driver][2]

 [1]: http://www.aircrack-ng.org/doku.php?id=mac80211 "mac80211"
 [2]: http://www.aircrack-ng.org/doku.php?id=iwl3945