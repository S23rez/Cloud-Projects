<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Query Data with DynamoDB

**Project Link:** [View Project](http://nextwork.ai/projects/aws-databases-query)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

## Query Data with DynamoDB

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-query_733d9399)

---

## Introducing Today's Project!

### What is Amazon DynamoDB?

What is Amazon DynamoDB and why is it useful?

Amazon DynamoDB is a non-relational database used for storing data. It usefulness lies in its speed, flexibility and efficiency to query and populate data. The architecture is managed by AWS and it's serverless. No matter how much data is in the database it's speed is always in miliseconds.

### How I used Amazon DynamoDB in this project

In today's project, I used Amazon DynamoDB to create a database with AWS Cloushell and also siphon some of it's features such as project-expression, transactions, RCUs, consistent-read and others.

### One thing I didn't expect in this project was...

One thing I didn't expect in this project is how transactions worked.

### This project took me...

This project took me couples of hours.

---

## Querying DynamoDB Tables

A partition key is is equivalent to a primary key used to filter and find data in a non-relational database. Partition key is not unique.

A sort key is an optional/subordinate of a partition key, in the stead where we have same partition keys for various attributes, a unique sort key have to be attached to these partition keys in order to filter data efficiently. This combination is known as composite key.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-query_d105b0b0)

---

## Limits of Using DynamoDB

I ran into an error when I queried for post by a particular user. This was because I didn't provide a partition key in my query.

Insights we could extract from our Comment table includes the total number of items and attributes in the table. Insights we can't easily extract from the Comment table includes comments by a user.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-query_cb3e260c)

---

## Running Queries with CLI

A query I ran in CloudShell was: aws dynamodb get-item \
    --table-name ContentCatalog \
    --key '{"Id":{"N":"202"}}' \
    --projection-expression "Title, ContentType, Services" \
    --return-consumed-capacity TOTAL
 This query will return the most recent/updated item with Id 202 in ContentCatalog, with selected item filters i.e  ContentType, Title e.tc and also the total RCUs consumed.

Query options I could add to my query are:

--key '{"Id":{"N":"202"}}' (get item in this primary key)
--projection-expression "Title, ContentType, Services" (Only these attributes)
--return-consumed-capacity TOTAL (RCUs consumed)


![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-query_733d9399)

---

## Transactions

A transaction is a way of organizing various commands that connects related tables in a non-relational database. i.e the first commands can put item into a table and update same in another. However, if there's an error at any point the command doesn't function at any level.

I ran a transaction using AWS CloudShell. This transaction did two things, populate attributes into a table and update another table with number of data populated in the other.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-databases-query_2f65f83e)

---

---
