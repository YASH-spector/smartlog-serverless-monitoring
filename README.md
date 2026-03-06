# smartlog-serverless-monitoring
Serverless log monitoring platform built using AWS Lambda, API Gateway, DynamoDB, and CloudWatch.
I built a serverless log monitoring system on AWS. Applications send logs through an API Gateway endpoint, which triggers a Lambda function to process the logs. The structured log metadata is stored in DynamoDB, while raw logs are archived in S3. CloudWatch monitors log patterns, and SNS can send alerts when error thresholds are exceeded. The infrastructure can also be deployed automatically using CloudFormation


I built a serverless log monitoring platform on AWS that processes application logs in real time and automatically alerts when errors occur.
Applications send logs through an API endpoint created using Amazon API Gateway, which triggers a AWS Lambda function to process the logs.
The Lambda function parses the logs, stores structured metadata in Amazon DynamoDB, and archives the raw logs in Amazon S3.
If the system detects logs with an ERROR level, it automatically sends notifications using Amazon Simple Notification Service.
I also integrated Amazon CloudWatch for monitoring and alarms, and used AWS CloudFormation to automate infrastructure provisioning.
