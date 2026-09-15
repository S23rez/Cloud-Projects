<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Creating a Private Subnet

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-private)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Creating a Private Subnet

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-private_afe1fdbd)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is an isolated virtual network in AWS. It is useful because it helps privatize one's own network in AWS.

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to create a private subnet, route table, NACL.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project is nothing

### This project took me...

This project took me couple of hours

---

## Private vs Public Subnets

The difference between public and private subnets is that one is available to the public and other is not

Having private subnets are useful because they held keep resources confidential

My private and public subnets cannot have the same IPv4 subnet CIDR block in order not to overlap

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-private_afe1fdbd)

---

## A dedicated route table

By default, my private subnet is associated with nothing

I had to set up a new route table because the other route has other rules and it's also attached to internet gateway meant for the public

My private subnet's dedicated route table only has one inbound and one outbound rule that allows local traffic equivalent to my VPC IPv4 address

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-private_b4b904b5)

---

## A new network ACL

By default, my private subnet is associated with a default NACL that allows and send HTTP packets to all IPv4 destinations.

I set up a dedicated network ACL for my private subnet because I don't want anyone sending to it and otherwise and also to prevent lateral atatck if an attacker gains access to my public subnet.

My new network ACL has two simple rules deny all traffics inbound and outbound.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-private_1ed2cb07)

---

---
