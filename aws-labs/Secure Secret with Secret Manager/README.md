<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Secure Secrets with Secrets Manager

**Project Link:** [View Project](https://nextwork.ai/projects/d6a05ea4-6c31-5e53-8688-de54814d6209)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_r7s8t9u0)

## Introducing Today's Project!

In this project, I will demonstrate the use of AWS Secrets Manager to store credentials as variable. I'm doing this project to learn about security.

### Tools and concepts

### Project reflection

## Hardcoding credentials

In this project, a sample web app is exposing credentials. It is unsafe to harcode credentials because anyone can access the web app.

I've set up the initial configuration with AWS credentials (variables and values). These credentials are just examples because it's for testing.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_j2k3l4m5)

## Using my own AWS credentials

As an extension for this project, I also decided to to set up my virtual environment, I installed boto3 for python and the requirements needed.

When I first ran the app, I ran into an error because the credentials are not valid

To resolve the 'InvalidAccessKeyId' error, I updated the config.py with real access keys from AWS IAM.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_wghjteykut)

## Pushing Insecure Code to GitHub

Once I updated the web app code with credentials, I forked the repository because I want to have a copy of the repo in my person github account and modify it. A fork is different from a clone because a fork is like getting a copy of a repo into one's repo online, while cloning is also copying a repo but offline.

To connect my local repository to the forked repository, I... updated the remote URL using git remote add origin <forked-repo-url>) so Git knows where to direct fetch and push operations. Then I used git add and git commit to stage the modified files and a snapshot message. Finally, git push uploads my local commits to the remote repo i.e origin main.

GitHub blocked my push because a  secret was insecure in the commit. This is a good security feature because it helps the developer notice security flaws in code before deployment.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_o2p3q4r5)

## Secrets Manager

Secrets Manager is an AWS service that helps store sensistive and secretive informations. I'm using it to store AWS Access Key and Secret Key ID. Other common use cases include API keys and database credentials.

Another feature in Secrets Manager is secret rotation which means it changes the secrets (i.e password) over a specified time. It's useful in situations where the asset is high value and this rotation helps minimize attack surface i.e if an attacker breach the website or resources, rotation can help mitigate the time of the attack.

Secrets Manager provides sample code in various languages, like Python3, Ruby, Go, rust, PHP, Javascript, Java. This is helpful because various developers can embed the sample code in their codes.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_h2i3j4k5)

## Updating the web app code

I updated the config.py file to retrieve the credential from AWS Secret Key service. The get_secret() function will retrieve the secret using it's various variables and values.

I also added code to config.py to extract the secret in JSON format. This is important because our code is python and json makes the secret easier to parse into python variables.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_v0w1x2y3)

## Rebasing the repository

Git rebasing is used to rewrite commit history. I used it to drop a commit that contains hardcoded credentials. This was necessary because without dropping that commit I can't move forward.

A merge conflict occurred during rebasing because the same lines of codes were being changed in different commits. I resolved the merge conflict by manually removing the conflicting version.

Once the merge conflict was resolved, I verified it by checking the code in Github.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d6a05ea4-6c31-5e53-8688-de54814d6209_t5u6v7w8)

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/d6a05ea4-6c31-5e53-8688-de54814d6209)*
