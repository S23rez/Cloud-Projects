<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Connect a Web App with Aurora

**Project Link:** [View Project](http://nextwork.ai/projects/aws-databases-webapp)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Connect a Web App to Amazon Aurora

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-webapp_1709b26b)

---

## Introducing Today's Project!

### What is Amazon Aurora?

Amazon Aurora is a relational database compatible with MySQL and PostgreSQL, it is useful because it provides a cluster feature seperating read and write making data available in replicas with high efficiency.

### How I used Amazon Aurora in this project

In today's project, I used Amazon Aurora to create a relational database and attach it to a web server.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project was how explanatory and practical driven it is.

### This project took me...

How much time did this project take you? an hour

---

## Creating a Web App

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-webapp_b7999168)

To connect to my EC2 instance, I ran the command ssh -i NextWorkAuroraApp.pem ec2-user@ec2-13-220-86-216.compute-1.amazonaws.com.

To help me create my web app, I first updated the dependencies on my Amazon linux. Afterwards I downloaded the dependencies need for my Web App and MySQL i.e http, php-mysqli, mariabd105. I ran this command http://ec2-13-220-86-216.compute-1.amazonaws.com/ on my browser as well and it was success "It works!".

---

## Connecting my Web App to Aurora

I set up my EC2 instance's connection details to my database by navigating to the /var/www directory on my EC2 instance, resolved a permission denied error by using sudo chown to transfer folder ownership from root to ec2-user, and created a new subfolder named inc. Inside that folder, I created a configuration file called dbinfo.inc using the nano text editor and added the PHP configuration block containing our database credentials (admin username, database name, and password) alongside the database endpoint retrieved directly from the AWS database console.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-webapp_1709b25b)

---

## My Web App Upgrade

Next, I upgraded my web app by navigating to /var/www/html, created a SamplePage.php file and added a code that pulls the details from the dbinfo.inc file created earlier and using it to display up-to-date changes directly from our website.and also changed the layout of the web page.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-webapp_2709b25b)

---

## Testing my Web App

To make sure my web app was working correctly, I installed the MySQL CLI client on my EC2 instance and connected directly to my database endpoint over port 3306 using the mysql -h <endpoint> -P 3306 -u admin -p command. Once authenticated, I switched to the target schema with USE sample; and ran the query SELECT * FROM EMPLOYEES;, which displayed the exact rows and entries I had previously submitted through the web application's frontend form.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-webapp_1409z22b)

---

---
