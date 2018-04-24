---
title: Regular Expression
author: felipe
type: post
date: 2010-02-02T03:14:32+00:00
url: /regular-expression/
categories:
  - Australia

---
Previously we have an [example on regular expression][1], but It doesn’t shows the power of square brackets ( [ ] )

Let say you want to search for string fprintf, vprintf and sprintf using grep, usually what you do is

<pre>egrep "fprintf|vprintf|sprintf" *.c</pre>

You may be ask why don’t just uses the word “printf”? If uses the word printf, it will return all of them but also include printf itself. But in this case i don’t want to grep other printf besides f,v,s printf. Thats the square brackets comes in to lessen your trouble.

<pre>egrep "[sfv]printf" *.c</pre>

It simply return the result with any character specified in [ ] with word printf concatenated.

The square brackets can be used with other RE symbols, here is another example, let say I want to gets all lists with words start with a character “a to f”, I can do this

<pre>egrep "^[a-f]" com-book.txt</pre>

It is case sensitive, I want all a to f including the upper case A to F.

<pre>egrep "^[a-fA-F]" com-book.txt
</pre>

[Copyright: ByExample.com][2]

 [1]: http://lne.blogdns.com/lbe/archives/92/regular-expression-with-egrep-and-ls/
 [2]: http://linux.byexamples.com/