<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Encrypt Data with AWS KMS

**Project Link:** [View Project](https://nextwork.ai/projects/716e7f81-84d1-51d6-8945-d4860caebf77)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_w0x1y2z3)

## Introducing Today's Project!

In this project, I will demonstrate using AWS KMS (Key Management System) to protect Database. The goal is to create encryption keys with KMS, encrypt a DynamoDB's table data with that key, then test access using IAM users .

### Tools and concepts

Services I used include KMS, DynamoDB and IAM. Key concepts I learnt include encryption,  decryption and access management using policies.

### Project reflection

This project took me approximately some hours.. The most challenging part was logging into the test user. It was most rewarding to actually see the encryption polivy take effect.

I chose to do this project today because I want to be a Cloud Security Engineer. Something that would make learning with NextWork even better is keep delivering the best conent. Thank you

## Encryption and KMS

Encryption is the process of turning a plain text into a ciphertext using alhorithms.Companies and developers do this to protect data at areat and in ttansits. Encryption keys are ciphertexts that can only be cracked by the algorithm used. 

AWS KMS is an encyrption vault in AWS used to create, manage and use encryption keys. Key management systems are important because it makes management activities such as, acess, logs, molbility and security flexible.

Encryption keys are broadly categorized as symmentric and asymmetric. I set up a symmetric key because I want a single key for both encryption and decryption process.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_a2b3c4d5)

## Encrypting Data

My encryption key will safeguard data in DynamoDB, which is a non-relational database. It is fast and flexible.

The different encryption options in DynamoDB include, Owned by Amazon DynamoDb, AWS managed key, and customer owned. Their differences are based on the management policies. I selected customer owned key, so I can have access to my key.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_q8r9s0t1)

## Data Visibility

Rather than controlling who has access to the key, KMS manages user permissions by controlling what a user can do with the key i.e our test user could see the key, but it needs permission to decrypt.

Despite encrypting my DynamoDB table, I could still see the table's items because I am an Admin user. DynamoDB uses transparent data encryption, which means it doesn't need to re-verify or otherwise it does the encryption/decryption method for me.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_c0d1e2f3)

## Denying Access

I configured a new IAM user to test the encryption in my DynamoDB. The permission policies I granted this user are DynamoDB FullAccess but not Administrator access.

After accessing the DynamoDB table as the test user, I encountered an Access denied error because I am not authorized to decrypt the data in the DynamoDB database. This confirmed that my encryption rule is active.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_w0x1y2z3)

## EXTRA: Granting Access

To let my test user use the encryption key, I added the user as a key user in KMS. My key's policy was updated to the test user being able to encrypt/decrypt with the key.

Using the test user, I retried accessing the database and I observed it gave me permission to view the data which confirmed that the test user now has access to encrypt and decrypt.

Encryption secures data instead of a resource. I could combine encryption with access control or security groups to protect data at the resource level and also within the resource.

![Image](https://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/716e7f81-84d1-51d6-8945-d4860caebf77_feffb2fb8)

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/716e7f81-84d1-51d6-8945-d4860caebf77)*
