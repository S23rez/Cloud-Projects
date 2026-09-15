<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# VPC Monitoring with Flow Logs

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-monitoring)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## VPC Monitoring with Flow Logs

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_3e1e79a1)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is great and it is useful because it covers a lot on networking and monitoring.

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to monitor flow logs.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how insightful it was.

### This project took me...

This project took me some hours.

---

## In the first part of my project...

### Step 1 - Set up VPCs

In this step, I will set up network monitoring using VPC Flow logs and AWS Cloudwatch because Network monitoring involves tracking the performance and security of my VPC's traffic.

### Step 2 - Launch EC2 instances

In this step, I will launch an instance in the two VPCs because I need to test the connection.

### Step 3 - Set up Logs

In this step, I will set up VPC Flow logs and set up a storage space for my flow logs because flow logs can be used to monitor network traffic.

### Step 4 - Set IAM permissions for Logs

In this step, I will give my VPC Flow logs the permission to write and send logs to Cloudwatch because without the IAM permission it can't write to  Cloudwatch.

---

## Multi-VPC Architecture

I started my project by launching two VPCs. I created one public subnet each on the two VPCs.

The CIDR blocks for VPCs 1 and 2 are 10.1.0.0/24 and 10.2.0.0/24. They have to be unique because without being unique their IPs will overlap.

### I also launched EC2 instances in each subnet

My EC2 instances' security groups allow  SSH and ICMP. This is because I need to access my instance using AWS Instance Connect through SSH protocol and ICMP for network availability testing.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_e7fa8775)

---

## Logs

Logs are metrics and datas of whatever happens in ones machine or in AWS, resources one has running and activities on these resources. They can also be seen as everyday and everytime journal entry of activities on one's machine.

Log groups are a way of cummulating or bringing together logs that relates to each other i.e network or system logs.

### I also set up a flow log for VPC 1

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_e8398869)

---

## IAM Policy and Roles

I created an IAM policy because my VPC Flow logs doesn't have the permission to write and pupulate logs into AWS Cloudwatch Log groups.

I also created an IAM role because VPC flow logs needs the permission to write and upload logs to Cloudwatch

A custom trust policy is a way of writing policies for a specific resources/user to access an IAM role.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_4334d777)

---

## In the second part of my project...

### Step 5 - Ping testing and troubleshooting

In this step, I will set up VPC peering connection to send traffic from one resource to another because it will get logs and send them to my Flow logs and I can analyze the network logs.  

### Step 6 - Set up a peering connection

In this step, I will peer my VPCs because it is needed for my VPCs to talk to each other privately.

### Step 7 - Analyze flow logs

In this step, I will look at the logs being recorded in the VPC Flow logs.

---

## Connectivity troubleshooting

My first ping test between my EC2 instances had no replies, which means there's an issue with the security group/Network ACL blocking ICMP traffic.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_99d4ba42)

I could receive ping replies if I ran the ping test using the other instance's public IP address, which means my second instance is actually allowing ICMP traffic.

---

## Connectivity troubleshooting

Looking at VPC 1's route table, I identified that the ping test with Instance 2's private address failed because there's no route connecting the two VPC's together thereby private connection is not established.

### To solve this, I set up a peering connection between my VPCs

I also updated both VPCs' route tables so that even when the VPCs are peered without provisioning a route they still don't know how to talk to each other.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_7316a13d)

---

## Connectivity troubleshooting

I received ping replies from Instance 2's private IP address! This means the two instances can communicate with each other now.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_4ec7821f)

---

## Analyzing flow logs

Flow logs tell us about the analysis of the network traffic.

For example, the flow log I've captured tells us about the Source, Dest IPs, time, port number and other network stats.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_d116818e)

---

## Logs Insights

Logs Insights is a feature on AWS that gives you explanatory details of logs.

I ran the query SOURCE "arn:aws:logs:us-east-1:873938828571:log-group:NextWorkVPCFlowLogsGroup" START=-1h END=0s |
fields @timestamp, @message
| sort @timestamp desc
| limit 10. 

This query analyzes the first ten network activities of flow logs.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-monitoring_3e1e79a1)

---

---
