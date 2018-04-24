---
title: Amazon VPC is not a network and does not provide a measure of security
author: felipe
type: post
date: 2017-08-14T10:27:23+00:00
url: /amazon-vpc-is-not-a-network-and-does-not-provide-a-measure-of-security/
categories:
  - AWS
tags:
  - aws
  - ec2
  - vpc

---
A VPC, or virtual private cloud, does not offer security. It is only a container, inside which subnets are created. AWS resources are launched inside of a subnet. EC2 instances make use of Security Groups for their security. Subnets provide an additional layer of security in the form of Network Access Control Lists. The combination of Security Groups, and Network ACLs are what provide security to EC2 instances. VPCs themselves are not networks, and AWS resources cannot be placed inside of them (other than subnets, Internet Gateways, and VPC endpoints, none of which the customer is required or expected to &#8220;secure&#8221;)