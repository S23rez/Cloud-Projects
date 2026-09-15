<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a Virtual Private Cloud

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-vpc)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Build a Virtual Private Cloud (VPC)

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-vpc_2facf927)

---

## Introducing Today's Project!

In this project, I will demonstrate how to us the Virtual Private Cloud. I'm doing this project to learn and understand properly the Networking structure of the Cloud

### What is Amazon VPC?

Amazon VPC is the private area you have in AWS and it is useful because it helps your resources stay private and you get to manage how they interact with the public internet.

In today's project, I used Amazon VPC to create an IP address and CIDR, Public Subnet and Internet gateway.

### Personal reflection

This project took me some couple of hours.

One thing I didn't expect in this project was using the CLI and also getting errors.

---

## Virtual Private Clouds (VPCs)

### What I did in this step

In this step, I will create a VPC because I want to better understand the concept of internet in the cloud

### How VPCs work

VPCs are an isolate cloud in AWS once can use to make their resources private

### Why there is a default VPC in AWS accounts

There was already a default VPC in my account ever since my AWS account was created. This is because AWS set up a default VPC to route my resources to the internet without creating one myself.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-vpc_2facf927)

### Defining IPv4 CIDR blocks

To set up my VPC, I had to define an IPv4 CIDR block, which is  way of defining the amount of IP adresses I want to use for my AWS resources

---

## Subnets

### What I did in this step

In this step, I will create a Public Subnet because it allows any resource launched inside the subnet gets a public IP address.

### Creating and configuring subnets

Subnets are the individual networks in a VPC. There are already subnets existing in my account, one for every availability domains.

### Public vs private subnets

The difference between public and private subnets are that public subnets are used for resources facing the public internet i.e a web server, while a private subnet is used for resources with confidential stuffs i.e database. For a subnet to be considered public, it has to be connected to an Inetrnet gateway.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-vpc_157c4219)

### Auto-assigning public IPv4 addresses

Once I created my subnet, I enabled auto assign public IPv4 address. This setting makes sure any resource I launch under this subnet gets an automatic Public IPv4 address so that it can communicate with the public internet.

---

## Internet gateways

### What I did in this step

In this step, I will create an internet gateway and attach it to my VPC because without it the resources in my VPC cannot access the internet.

### Setting up internet gateways

Internet gateways are key VPC components that allows resources from the VPC/subnets access the internet.

Attaching an internet gateway to a VPC means the resources in the VPC through the public subnet can reach the public internet. If I missed this step the resources in the VPC won't be able to reach the internet.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-vpc_4ae90410)

---

## Using the AWS CLI

### What I'm doing in this extension

In this project extension, I will launch my cloudshell because I want to use AWS CLI commands to set up a VPC, subnet and internet gateway

### Exploring CloudShell and CLI

VPC resources could also be created with CloudShell, which is a shell that comes preinstalled in AWS. CLI is used to run and automate task, and also it is very fast unlike GUI.

### Debugging my setup

To set up a VPC or a subnet, you can use the command: 
aws ec2 create-tags --resources=VPC-ID --tags Key=Name,Value="NextWork VPC 2" and aws ec2 create-subnet --vpc-id VPC-ID --cidr-block ADD-CIDR-BLOCK-HERE

 Make sure to avoid errors by including your own VPC-ID and CIDR Block

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-vpc_9b2465411)

### Comparing CloudShell vs AWS Console

Compared to using the AWS Console, an advantage of using commands is that it is very fast and it flags error which makes it hard to make mistaake. An advantage of using the Console is it makes it better to understand the architecture. Overall, I preferred both.

---

---
