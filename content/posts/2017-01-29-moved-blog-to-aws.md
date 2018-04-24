---
title: Moved blog to AWS
author: felipe
type: post
date: 2017-01-28T15:18:16+00:00
url: /moved-blog-to-aws/
tc-thumb-fld:
  - 'a:2:{s:9:"_thumb_id";i:883;s:11:"_thumb_type";s:10:"attachment";}'
categories:
  - AWS
  - computers
  - technology
tags:
  - aws
  - cloud
  - t2.micro

---
I have just migrated my blog from my previous host j u s t h o s t to Amazon Web Services. Even on just a humble T2.micro, the speed is noticeably quicker. I have MySQL running on the same host, with no load balancers, and just an Elastic IP Address and Route 53 A Record pointing to it. I still need to figure out a way to automate a daily Ec2 Snapshot, with deletes after 14 days.