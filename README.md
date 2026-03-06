# smartlog-serverless-monitoring
Serverless log monitoring platform built using AWS Lambda, API Gateway, DynamoDB, and CloudWatch.
I built a serverless log monitoring system on AWS. Applications send logs through an API Gateway endpoint, which triggers a Lambda function to process the logs. The structured log metadata is stored in DynamoDB, while raw logs are archived in S3. CloudWatch monitors log patterns, and SNS can send alerts when error thresholds are exceeded. The infrastructure can also be deployed automatically using CloudFormation
