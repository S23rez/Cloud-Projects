<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Cloud Security with AWS IAM

**Project Link:** [View Project](http://nextwork.ai/projects/aws-security-iam)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_1c864649)

---

## Introducing Today's Project!

### Project overview

In this project, I will demonstrate how to create EC2 instances, and spin up IAM and policies to attach to the EC2 resources I'm doing this project to learn about authorization and authentication in the cloud

### Tools and concepts

Services I used were IAM, EC2 Key concepts I learnt include IAM Policy Simulation, Instances, Account alias, group users, IAM users, policies, Tags, policies and how JSON policies work, user csv file, regions, iso and others

### Project reflection

This project took me approximately three days The most challenging part was trying to understand the JSON policies. It was most rewarding to see that the dev-group was denied a lot of access andf seeing it in real time is mind-blowing.

---

## Tags

### What I did in this step

In this step, I will launch to EC2 instances because we need boost Nextwork's computing power for the summer break

### Understanding tags

Tags are organizational tools that are used to group resources for ease of reference i.e. billing costs, policies and others

### My tag configuration

The tag I’ve used on my EC2 instances is called Env meaning Environment. The value I’ve assigned for my instances are Production and Development.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_2e0e5a5d)

---

## IAM Policies

### What I did in this step

In this step, I will create an IAM policy to manage RBAC for the new interns because I want them to have access only to a specific instance i.e the development env and not the production env.

### Understanding IAM policies

IAM Policies are rules in the cloud that works for authentication meaning who can do what to the resources.

### The policy I set up

For this project, I’ve set up a policy using JSON format

### Policy effect

I’ve created a policy that allows a user to do anything they want to any instances tagged "Development", they can also see every other instances but they cannot delete/create any tags.

### Understanding Effect, Action, and Resource

The Effect, Action, and Resource attributes of a JSON policy means Effect decides whether the rule permissions are granted or blocked using either "Allow" or "Deny". Action specifies the specific API operations or tasks being targeted (such as "s3:GetObject" or "ec2:StartInstances"), while Resource identifies the exact AWS assets (like a specific bucket ARN or "*" for all assets) that the actions are allowed or denied to run against.

---

## My JSON Policy

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_1c864649)

---

## Account Alias

### What I did in this step

In this step, I will setup an account alias which is like a nickname for an aws console login because it makes it easier for a user to login

### Understanding account aliases

An account alias is like a nickname which makes it easier to login to the Console rather than using the account ID

### Setting up my account alias

Creating an account alias took me couple of mins Now, my new AWS console sign-in URL is https://prod-alias-----------.signin.aws.amazon.com/console

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_0eb4439b)

---

## IAM Users and User Groups

### What I did in this step

In this step, I will set up IAM users and IAM users groups because IAM users are people who can login to the console and the IAM users group is where we can group different users with same policies

### Understanding user groups

IAM user groups are kind of an organization resource where you add users who share same policies

### Attaching policies to user groups

I attached the policy I created to this user group, which means the defined in the rules will affect the user group

### Understanding IAM users

IAM users are are users who can login into the Console and access resources 

---

## Logging in as an IAM User

### Sharing sign-in details

The first way is to Email sign in instructions while the other is to download the .csv file and send 

### Observations from the IAM user dashboard

Once I logged in as my IAM user, I noticed that some access priviledges were denied. This was because of the policy attached to the user group making our user footprint limited in the console.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_6f2ab446)

---

## Testing IAM Policies

### What I did in this step

In this step, I will login to AWS using the intern access because I want to test if the access given to the intern is affective.

### Testing policy actions

I tested my JSON IAM policy by trying to stop both the prod and dev instances.

### Stopping the production instance

When I tried to stop the production instance it denied the access. This was because of the policy attached

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_0e7a9d6a)

### Stopping the development instance

Next, when I tried to stop the development instance it worked and displayed stopping. This was because the group access was able to stop the dev instance.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_1811801c)

---

## IAM Policy Simulator

To extend my project, I'm going to use the IAM Policy simulator to test my policies. I'm doing this because testing polict directly on the console will disrupt workflow, thereby I will usethe IAM Policy simulator where I can check if a policy is effective without disrupting workflow.

### Understanding the IAM Policy Simulator

The IAM Policy Simulator is a tool on AWS IAM console that enables you test policy in real time without disrupting workflow It's useful for testing policies and access in IAM, it's also brilliant because you don't need to login to another user. It is fast and efficient.

### How I used the simulator

I set up a simulation for the development instance (DeleteTags and Stop Instances). The results were both denied on the first try I had to adjust the StopInstance resource and change it to Development and I got allowed after re-running the simulation.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-security-iam_069d8a621)

---

---
