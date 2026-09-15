<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Load Data into DynamoDB

**Project Link:** [View Project](http://nextwork.ai/projects/aws-databases-dynamodb)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Load Data into a DynamoDB Table

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_b481c730)

---

## Introducing Today's Project!

### What is Amazon DynamoDB?

What is Amazon DynamoDB and why is it useful?

Amazon DynamoDB is a non-relational database used to store data and it is useful because it is flexible and fast.

### How I used Amazon DynamoDB in this project

In today's project, I used Amazon DynamoDB to create table and upload data into the database.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project is how Cloudshell makes the creation and uploading seamless.

### This project took me...

This project took me couple of hours.

---

## Create a DynamoDB table

DynamoDB tables organises data using items and attributes(keys+values).

An attribute is a component that holds the key and value of a data.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_a3cefee0)

---

## Read and Write Capacity

Read capacity units (RCUs) and write capacity units (WCUs) are engines provisioned for both read and write requests. They work on a per second scale, however, while 2 items read per second uses 1 RCU engine, 2 wrire per second uses 2 WCU engines.

Amazon DynamoDB's Free Tier covers 25 WCU/RCU per second of the month and also 25gb free data storage.  I turned off auto scaling because it might get the WCU/RCU out of threshold based on traffic.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_ef47dd8f)

---

## Using CLI and CloudShell

AWS CloudShell is browser based shell where you can write out commands to access AWS resources using the AWS CLI. It offers 1gb storage in the terminal home directory within that AWS region.

AWS CLI is the open-source command line of AWS used to access AWS resources on CloudShell or local terminal.

I ran a CLI command in AWS CloudShell that created 4 tables, ID, Types and their status.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_81e0258b)

---

## Loading Data with CLI

I ran a CLI command in AWS CloudShell that uploaded all datas into their respective tables i.e aws dynamodb batch-write-item --request-items file://Comment.json for Comment Table.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_791c600b)

---

## Observing Item Attributes

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_b481c731)

I checked a ContentCatalog item, which had the following attributes: Key:Id ; Value:1.

I checked another ContentCatalog item, which had a different set of attributes unique to it i.e ContentType, Price, Services, Title, URL, VideoType.

---

## Benefits of DynamoDB

A benefit of DynamoDB over relational databases is flexibility, because is not rigid to rows and columns being relational. Items in a DynamoDB table can have different row(Items) and columns(attributes) carry different data types simultaneously.

Another benefit over relational databases is speed, because it's easy querying the database using the primary key and also adding new rows and columns without altering the whole table.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-dynamodb_b481c730)

---

---
