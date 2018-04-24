---
title: Secret or Hidden page in Linksys WAG54g2 ADSL Modem and Wireless Router
author: felipe
type: post
date: 2010-09-12T05:45:53+00:00
url: /secret-or-hidden-page-in-linksys-wag54g2-adsl-modem-and-wireless-router/
categories:
  - technology

---
Trying to Google this problem was very frustrating. Hopefully it will help someone else. The Linksys WAG54G2 ADSL modem + Wireless Router does not have a GUI page to show more technical information, such as line attenuation, among others.

Therefore, there are some secret or hidden pages built into the device that will reveal this information. The router&#8217;s default IP address is 192.168.1.1, but if you have changed yours, the links won&#8217;t work, and you _should_ know what to do.

  * First, ensure it is in &#8216;debug&#8217; mode 
      * <http://192.168.1.1/setup.cgi?todo=debug>
  * Then click on this link 
      * [http://192.168.1.1/setup.cgi?next\_file=adsl\_driver.htm][1]

 [1]: http://192.168.1.1/setup.cgi?next_file=adsl_driver.htm