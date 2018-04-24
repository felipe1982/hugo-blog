---
title: File Shredder
author: felipe
type: post
date: 2009-04-30T12:18:25+00:00
url: /file-shredder/
categories:
  - software
tags:
  - geek
  - privacy
  - security
  - software

---
<img class="alignright size-thumbnail wp-image-262" title="shredder" src="http://www.felipe.com.au/blog/wp-content/uploads/2009/05/shredder-150x150.png" alt="shredder" width="150" height="150" />Typically, when you &#8216;delete&#8217; a file, you are only detaching the link from your filesystem to the actually binary data on the physical platters of your hard drive. The data aren&#8217;t really _gone_. The filesystem declares this space as &#8216;free&#8217; or &#8216;available&#8217;, and so only goes away when that space is overwritten by new data.

If you&#8217;ve ever desire to _truly_ delete a file, then download [file shredder][1]. It allows you you select and right click any file, and it automatically overrights them with random data, stuffs it full of zeros, and then deletes it. This prevents anyone from ever recovering that file with forensic software. Larger files take longer to shred, but are usually shredded in under 1 minute. If I coulf find the author&#8217;s email, I&#8217;d ask him/her to add a right-click to &#8220;shred all files in the recycle bin.&#8221;

 [1]: http://fileshredder.org/