<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Testing VPC Connectivity

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-connectivity)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Testing VPC Connectivity

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_8ee57662)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is a virtual isolated network where one can manage resources access to the internet on AWS and it is useful because it really helps with rules and security

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to simulate a public and private web server communication

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how intsense and explanatory it was

### This project took me...

This project took me some hours

---

## Connecting to an EC2 Instance

Connectivity means getting resources in my network to communicate/send traffic to each other and external network based on the rules. 

My first connectivity test was whether I could connect to my Nextwork Public Server

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_88727bef)

---

## EC2 Instance Connect

I connected to my EC2 instance using EC2 Instance Connect, which is a feature provided by AWS to connect to one's EC2 easily from the console

My first attempt at getting direct access to my public server resulted in an error, because the security group on my instance did not allow ssh 

I fixed this error by editing my Security group and allowing ssh - IPv4 anywhere.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_1cbb1b88)

---

## Connectivity Between Servers

Ping is a way of checking if the network one is trying to get to is alive or online. I used ping to test the connectivity between public server and my private server.

The ping command I ran was ping 10.*.*.*

The first ping returned no packet. This meant the network is not alive

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_defghijk)

---

## Troubleshooting Connectivity

I troubleshooted this by allowing all ICMP IPv4 traffic on my Private server inbound and outbound NACL and inbound only for Security Group

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_4a9e8014)

---

## Connectivity to the Internet

Curl is used to grab or make request from the website.

I used curl to test the connectivity between my server and nextwork domain.

### Ping vs Curl

Ping and curl are different because ping is used to test connection while curl is used to make request.

---

## Connectivity to the Internet

I ran the curl command curl example.com which returned <!doctype html><html lang="en"><head><title>Example Domain</title><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-connectivity_8ee57662)

---

---
