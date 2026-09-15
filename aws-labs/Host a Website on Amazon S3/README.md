<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Host a Website on Amazon S3

**Project Link:** [View Project](http://nextwork.ai/projects/aws-host-a-website-on-s3)

**Author:** Odunuga Abd fattah  
**Email:** odunugaabdfattah@gmail.com

---

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_5d4474f9)

---

## Introducing Today's Project!

### Project overview

In this project, I will demonstrate... I'm doing this project to learn Amazon S3 Bucket

### Tools and concepts

Services I used were AWS S3 Bucket. Key concepts I learnt included bucket endpoint URL, static webiste, index.html and files, bucket policy and ACL 

### Time, challenges, and wins

This project took me approximately an hour. The most challenging part was understanding the difference between bucket policy and ACL. It was most rewarding to fully host the static website

---

## How I Set Up an S3 Bucket

### What I did in this step

In this step, I will create an AWS S3 bucket because I want to understand the process and also host a static webiste

### How long it took to create the bucket

Creating an S3 bucket took me couple of minutes being the first time and also I got to learn some new concepts like versioning, encryption, Bucket policy and ACL, unique bucket name because my initial name failed and some blocking and unblocking public access

### Region selection

The Region I picked for my S3 bucket was Virginia because its cheaper and closer to me

### Understanding bucket name uniqueness

S3 bucket names are globally unique! This means that it is unique to me and no other bucket in the world can posses same name unless i delete the bucket

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_ba6d42ad)

---

## Upload Website Files to S3

### What I did in this step

In this step, I will upload the default website files into my S3 Bucket because if theres no file there won't be a website to host

### Files I uploaded

I uploaded two files to my S3 bucket - they were and index.html file (structure) and a folder of images and assets (i.e gives the website an interface and functions).

### How the files work together

Both files are necessary for this project as index.html gives structure but it wont be relevant if its not given content and that's where the other folder comes in with images and assets to give the website full functionality

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_a265af88)

---

## Static Website Hosting on S3

### What I did in this step

In this step, I will make the website available to the world by hosting it because our files will remain files unless we host it on the internet

### Understanding website hosting

Website hosting means putting out your website on a computer (web server) designed for turning raw files into a website page people can visit

### How I enabled website hosting

To enable website hosting with my S3 bucket, I uploaded my index.html file and assets. Afterwards I clicked on the proeprties pane on my S3 buckets and scrolled downward to enable static website hosting and also input index.html as our indexed document i.e. the file we mean to host

### Access Control Lists (ACLs)

An ACL is a kind of Role Access Based Control in S3 because which makes you give permission and access to anyone trying to access the bucket and i enabled even though AWS indicated that bucket policy is better but hopefully we will look into bucket policy later on 

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_c22c54c0)

---

## Bucket Endpoints

### Understanding bucket endpoint URLs

Once static website is enabled, S3 produces a bucket endpoint URL, which is the URL that will take you to the website you are trying to host

### What I saw when I tested the endpoint

When I first visited the bucket endpoint URL, I saw 403 Forbidden error. The reason for this error was because the website files are still private and their access is needed to be managed seperately. They need to be public files too for them to be available to the public.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_22ce4daf)

---

## Success!

### What I did in this step

In this step, I will make the website available by going to the files in the bucket and make them public because this will enable us view the content of our website and bringing it to love

### How I resolved the 403 error

To resolve this 403 Forbidden error, I went back to the object pane on s3 bucket and checked by objects, clicked the icon options and select "Make Public using ACL", confirmed afterwards and refreshed the url. The error was gone and a new clean, beautiful and functional static website resolved.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_5d4474f9)

---

## Bucket Policies

### What I did in this extension

In this project extension I'm about to use bucket policy to control access to our object files I'm doing this so that we can stop people from deleting objects from the file

### Understanding bucket policies

An alternative to ACLs are bucket policies, which are resource-based access policies written in JSON format. The benefit of using bucket policies is that they centralize access control for the entire bucket and can target individual objects or folders using specific path rules and advanced conditions. While ACLs were historically used for individual object access control, AWS now considers them a legacy method and recommends disabling them entirely.

Furthermore, bucket policies offer high granularity and absolute authority—allowing you to explicitly allow or deny specific actions for any user (including the root user)—whereas ACLs only offer basic access control toggles such as READ, WRITE, or FULL_CONTROL.

![Image](http://nextwork.ai/hopeful_brown_agile_finger_lime/uploads/aws-host-a-website-on-s3_sm2sm2sm)

### What my bucket policy does

My bucket policy deny explicitly any user. I tested this by trying to delete an object and saw access denied

---

---
