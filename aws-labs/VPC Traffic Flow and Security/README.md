<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# VPC Traffic Flow and Security

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-security)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## VPC Traffic Flow and Security

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_92b0b0b4)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is an isolated virtual network dedicated for a AWS account console and its resources and it is useful because it helps privatize and secure ones resources

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to demonstrate traffic flow, from IG, Route Table, association, security groups and network ACLs

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was nothing

### This project took me...

This project took me couple of hours

---

## Route tables

Route tables are used for routing network traffic i.e within a VPC or to the public internet.

Routes tables are needed to make a subnet public because if they are not attached to the internet gateway the traffic from resources in the VPC wouldn't know how to find their way to the public internet.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_0a07b191)

---

## Route destination and target

Routes are defined by their destination and target, which mean where it is going and how it will deliver i.e 0.0.0.0/0 attached to an internet gateway means that any traffic on this route is bound for public internet through the internet gateway.

The route in my route table that directed internet-bound traffic to my internet gateway had a destination of 0.0.0.0/0 and a target of igw-0931a9081*****.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_0a07b191)

---

## Security groups

Security groups are securtity guards that work at the resource level of a VPC.

### Inbound vs Outbound rules

Inbound rules are policy set for traffic going into the network. I configured an inbound rule that allows all HTTP traffic from all IPv4 addresses.

Outbound rules are policy for traffic going from the resource to the internet. By default, my security group's outbound rule allows my resource to send any traffic to the public internet.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_92b0b0b4)

---

## Network ACLs

Network ACLs are security policy at the Subnet level that inspect and filter which data packets/traffic coming and going out of the subnet.

### Security groups vs. network ACLs

The difference between a security group and a network ACL is that security group works at the resource level and it's stateful, while Network ACL works at the Subnet Level and it is stateless, you have to set the DENY or ALLOW policy for both the inbound and outbound

---

## Default vs Custom Network ACLs

### Similar to security groups, network ACLs use inbound and outbound rules

By default, a network ACL's inbound and outbound rules will deny all traffic 

In contrast, a custom ACL’s inbound and outbound rules are automatically set to deny all inbound and outbound traffic

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_4faeb056)

---

## Tracking VPC Resources

I created additional resources (VPC, IG and SG) Instead of my usual region, I used us-east-2. Teams would use multiple regions to improve latency for end users and also protect from disaster.

EC2 Global View is a tool where you can find... I could even narrow down my search by filtering for the region and its resources. Without EC2 Global View, you'd have to go to each region and check out thier resources.

Now that I've learnt about EC2 Global View, I'd use it again to manage my regions and their resurces.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-security_b03ea6162)

---

---
