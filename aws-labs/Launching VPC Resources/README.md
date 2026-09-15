<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Launching VPC Resources

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-ec2)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Launching VPC Resources

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-ec2_8ee57662)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is a virtual isolated network in AWS and it is useful because it helps privatize ones network where one can launch various resources on that private network.

### How I used Amazon VPC in this project

I used Amazon VPC to create VPCs, subnets, SGs, IG, Route Tables, and also launched instances.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how enlightening it was

### This project took me...

This project took me couple of hours

---

## Setting Up Direct VM Access

Directly accessing a virtual machine means trying ssh into the virtual machine from a remote desktop to download packages, modify configurations or deployment.

### SSH is a key method for directly accessing a VM

SSH traffic means remote access to a machine using secure shell.

### To enable direct access, I set up key pairs

Key pairs are cryptograhpic keys that help engineers authenticate themselves when trying to access (SSH) into an instance.

A private key's file format means a format ones keypair come with i.e PDF, DOC but keypair comes with .PEM. My private key's file format was .pem (Privacy Enhanced Mail).

---

## Launching a public server

Start your response with '

I had to change my EC2 instance's networking settings by choosing the networking configurations I already orchestrated i.e VPC, Public Subnet, SG and NACL

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-ec2_88727bef)

---

## Launching a private server

My private server has its own dedicated security group because it is a private server and it will contain confidential files.

My private server's security group's source is my Public Security Group which means resources in my Public Security Group can have access to my Private server.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-ec2_4a9e8014)

---

## Speeding up VPC creation

I used an alternative way to set up an Amazon VPC! This time, I used the VPC and more.

A VPC resource map is visual representation of the flow of your VPC and its components.

My new VPC has a CIDR block of 10.0.0.0/16. It is possible for my new VPC to have the same IPv4 CIDR block as my existing VPC because they can't overlap. They are both two diferent Virtual Isolated network.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-ec2_1cbb1b88)

---

## Speeding up VPC creation

### Tips for using the VPC resource map

When determining the number of public subnets in my VPC, I only had two options either none or 1 in each availability zone. This was because it's AWS redundancy for availability to have at least one subnet for each availability zones.

The set up page also offered to create NAT gateways, which are a way our private subnet can get connected to the public internet. However, it is a one way traffic, outbound only.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-ec2_8ee57662)

---

---
