<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# VPC Endpoints

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-endpoints)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## VPC Endpoints

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_09bcaa8a)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is great and it is useful because it gives you the whole tea on AWS networking.

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to create endpoint and understand how one can access AWS resources privately using endpoint.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how insightful it was.

### This project took me...

This project took me some hours.

---

## In the first part of my project...

### Step 1 - Architecture set up

In this step, I will create a VPC and launch an instance under the network because  I need the VCP and its instance to access S3.


### Step 2 - Connect to EC2 instance

In this step, I will connect to my EC2 using the EC2 Instance Connect because I need it to access my S3


### Step 3 - Set up access keys

In this step, I will create an Access Key because I need it for getting access to S3 from my EC2 Instance.

### Step 4 - Interact with S3 bucket

In this step, I will use my Access keys to connect to S3 because it is important for the project. 

---

## Architecture set up

I started my project by launching a VPC and an instance.

I also set up S3 bucket and added some files in the bucket.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_4334d777)

---

## Access keys

### Credentials

To set up my EC2 instance to interact with my AWS environment, I configured Access Key, Secret Access Key, region and output format.

Access keys are credentials needed to access AWS resources from EC2 or third party apps.

Secret access keys are the password equivalent for access keys.

### Best practice

Although I'm using access keys in this project, a best practice alternative is to use an IAM role.

---

## Connecting to my S3 bucket

The command I ran was aws s3 ls. This command is used to list the resources in my S3.

The terminal responded with my S3 bucket name..This indicated that the access keys I set up is working.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_4334d778)

---

## Connecting to my S3 bucket

I also tested the command aws s3 ls s3://s23rez-s3-demo-bucket which returned the files in my bucket.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_4334d779)

---

## Uploading objects to S3

To upload a new file to my bucket, I first ran the command sudo touch /tmp/nextwork.txt. This command creates a new file in my /tmp directory.

The second command I ran was aws s3 cp /tmp/nextwork.txt s3://nextwork-vpc-project-s23rez. This command will upload the file in my /tmp directory to my S3.

The third command I ran was aws s3 ls s3://nextwork-vpc-project-s23rez, which validated that the file was uploaded.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_3e1e79a2)

---

## In the second part of my project...

### Step 5 - Set up a Gateway

In this step, I will set up a VPC endpoint because I need my EC2 instance to communicate to S3 privately.

### Step 6 - Bucket policies

I'm about to create a bucket policy that only allows traffic from my endpoint.

### Step 7 - Update route tables

In this step, I will test my VPC endpoint because I need to test the connectivity.

### Step 8 - Validate endpoint conection

In this step, I will go to the instance because I want to test if it can route to the S3.

---

## Setting up a Gateway

I set up an S3 Gateway, which is a path through which my EC2 can get through to S3 privately.

### What are endpoints?

An endpoint is a way to talk to resources in AWS privately.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_09bcaa8a)

---

## Bucket policies

A bucket policy is a way you set rules for who has access to your bucket.

My bucket policy will allow only connection from VPC endpoint.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_7316a13d)

---

## Bucket policies

Right after saving my bucket policy, my S3 bucket page showed 'denied access' warnings. This was because my root don't have accesss to make changes to my bucket.

I also had to update my route table because the connection needs a route.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_4ec7821f)

---

## Route table updates

To update my route table, I head to my endpoint and added my VPC to the route.

After updating my public subnet's route table, my terminal could return files from the s3.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_d116818e)

---

## Endpoint policies

An endpoint policy is a way to set rules for who gets access to your endpoint.

I updated my endpoint's policy by changing the Allow to Deny I could see the effect of this right away, because my VPC endpoint doesn't have access to S3 anymore.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-endpoints_3e1e79a3)

---

---
