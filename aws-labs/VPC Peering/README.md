<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# VPC Peering

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-peering)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## VPC Peering

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_88727bef)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is an virtual isolated network and it is useful because it helps segregate, secure and manage network to prevent clashing.

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to create two VPCs, launched instances in them and test VPC peering.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how satisfying it is.

### This project took me...

This project took me couple of hours.

---

## In the first part of my project...

### Step 1 - Set up my VPC

In this step, I will set up two VPCs because it is a requirement in this project.

### Step 2 - Create a Peering Connection

In this step, I will create a peer connection between my two VPCs to aid private communication between them because it is a requirement of this project.

### Step 3 - Update Route Tables

In this step, I will set up a route for the two VPCs tp communicate because without a route they can't get packets to eahc other.

### Step 4 - Launch EC2 Instances

In this step, I will launch two EC2 instances because I need to send packets from a resource in one VPC to another.

---

## Multi-VPC Architecture

I started my project by launching a subnet each for the two VPCs.

The CIDR blocks for VPCs 1 and 2 are 10.1.0.0/16 and 1.2.0.0/16. They have to be unique because we want to avoid IP overlapping

### I also launched 2 EC2 instances

I didn't set up key pairs for these EC2 instances as AWS manages a key for using instance connect.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_11111111)

---

## VPC Peering

A VPC peering connection is a way of connecting to VPCs together in order to share resources privately.

VPCs would use peering connections to share resources between VPCs privately.

The difference between a Requester and an Accepter in a peering connection is one is initating and the other has a choice to accept or decline.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_1cbb1b88)

---

## Updating route tables

After accepting a peering connection, my VPCs' route tables need to be updated because without a route there still won't be a path for communication/traffic.

My VPCs' new routes have a destination of. 10.1.0.0/16 and 10.2.0.0/16. The routes' target was the peering connection

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_4a9e8014)

---

## In the second part of my project...

### Step 5 - Use EC2 Instance Connect

In this step, I will connect to my instance using EC2 instance connect because I need to get communicate with the resources in my other VPC.

### Step 6 - Connect to EC2 Instance 1

In this step, I will connect to my instance using EC2 instance connect because I have associated it with an Elastic IP and it already gave a static IPv4 address.

### Step 7 - Test VPC Peering

In this step, I will send a packet to my second instance because it is required.

---

## Troubleshooting Instance Connect

Next, I used EC2 Instance Connect to my instance but it failed.

I was stopped from using EC2 Instance Connect as my instacne does not have a public Ip address.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_7685490c)

---

## Elastic IP addresses

To resolve this error, I set up Elastic IP addresses. Elastic IP addresses are static IP addresses one can assign to an instance so the IP does not change whenever the instance reloads or over a period of time.

Associating an Elastic IP address resolved the error because it gave the instance a public address.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_45663498)

---

## Troubleshooting ping issues

To test VPC peering, I ran the command ping.

A successful ping test would validate my VPC peering connection because it shows I can reach the other VPCs connection.

I had to update my second EC2 instance's security group because. I could not reach the network. I added a new rule that allows ICMP traffic from my VPCs IP address.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-peering_7a29d352)

---

---
