<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Access S3 from a VPC

**Project Link:** [View Project](http://nextwork.ai/projects/aws-networks-s3)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Access S3 from a VPC

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_3e1e79a2)

---

## Introducing Today's Project!

### What is Amazon VPC?

Amazon VPC is a virtual isolated private network in AWS that lets one manage network and spin up resources in that network and it is useful because it entails a lot of learning features about how resources works and interact in AWS.

### How I used Amazon VPC in this project

In today's project, I used Amazon VPC to launch a VPC. I created a public subnet in that VPC and launched an instance in the subnet. I accessed AWS S3 from my EC2 using IAM access key and AWS CLI.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how insightful it was.

### This project took me...

This project took me an hour.

---

## In the first part of my project...

### Step 1 - Architecture set up

In this step, I will a VPC with a public subnet and an EC2 instacne inside that subnet because we need the EC2 to interact with s3 through the VPC.

### Step 2 - Connect to my EC2 instance

In this step, I will connect to my EC2 instance using my EC2 Instance Connect.

### Step 3 - Set up access keys

In this step, I will create Access keys because my EC2 needs it to interact with other resources in my AWS.

---

## Architecture set up

I started my project by launching a VPC with Public subnet and an EC2 instance inside this subnet with SSH enabled.

I also set up an S3 bucket and uploaded two files in it.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_4334d777)

---

## Running CLI commands

AWS CLI is a software that allows one manage AWS console direct from one's local terminal or computer. I have access to AWS CLI because it's preinstalled into EC2 instance.

The first command I ran was aws s3 ls. This command is used to list the files in S3.

The second command I ran was "aws configure". This command is used to set up my EC2 Instance's credenials in order to access my AWS environment.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_e7fa8776)

---

## Access keys

### Credentials

To set up my EC2 instance to interact with my AWS environment, I configured EC2 using the 'aws configure' command which gave me access to the resources in my aws from my EC2 using access key, access key secret, default region and format.

Access keys are like username and pasword that allows my instance, application or computer interact with my AWS services/resources.

Secret access keys are the password equivalent to access keys.

### Best practice

Although I'm using access keys in this project, a best practice alternative is to use a role. We can create a role and give it the necessary permissions and attach same to our EC2 instance and detach afterwards.

---

## In the second part of my project...

### Step 4 - Set up an S3 bucket

In this step, I will create an S3 bucket  because I want to validate access to S3 from my instance.

### Step 5 - Connecting to my S3 bucket

In this step, I will head back to my instance because I want to access and modify files in my S3 from the EC2 terminal.

---

## Connecting to my S3 bucket

The first command I ran was aws s3 ls. This command is used to list the files in S3.

When I ran the command aws s3 ls again, the terminal responded with the bucket name I created in my S3. This indicated that my EC2 can talk to my S3, thereby my access key works.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_4334d778)

---

## Connecting to my S3 bucket

Another CLI command I ran was aws s3 ls s3://nextwork-vpc-project-s23rez which returned the files in the bucket.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_4334d779)

---

## Uploading objects to S3

To upload a new file to my bucket, I first ran the command 'sudo touch /tmp/test.txt'. This command creates a text file inside my /tmp folder.

The second command I ran was 'aws s3 cp /tmp/test.txt s3://nextwork-vpc-project-enter your name'. This command will copy the .txt file from from my /tmp folder to the s3 bucket.

The third command I ran was 'aws s3 ls s3://nextwork-vpc-project-s23rez which validated that the file is available in my s3 bucket.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-networks-s3_3e1e79a2)

---

---
