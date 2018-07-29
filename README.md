# Awsomechat App API Notes
vicc@inteletry.com

Built following online guide: [Serverless Stack](https://serverless-stack.com/#table-of-contents)

Logged in to AWS console under Awsomechat account

Backend credentials using AWS IAM
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources for your users. You use IAM to control who can use your AWS resources (authentication) and what resources they can use and in what ways (authorization).
    https://serverless-stack.com/chapters/what-is-iam.html

A basic Serverless project needs permissions to the following AWS services:

- **CloudFormation to create change set and update stack**
- **S3 to upload and store Serverless artifacts and Lambda source code**
- **CloudWatch Logs to store Lambda execution logs**
- **IAM to manage policies for the Lambda IAM Role**
- **API Gateway to manage API endpoints**
- **Lambda to manage Lambda functions**
- **EC2 to execute Lambda in VPC**
- **CloudWatch Events to manage CloudWatch event triggers**

Created these DynamoDB tables:
User
    - email
    - Name
    - Phone Number

Company
    - Company_id
    - Company_name
Chat
 - Chat_id
 - initiated_by
 - initiated_on

Conversations
    - Conversation_ID
    - Timestamp
    - Messages
    - chat_id
    - participant id


Conversation_participants
    - participant_id 
    - company_id/User Id
    - joined_chat_On
    - left_chat_on

S3 Bucket for uploads
Enabled CORS

Cognito User Pool
awsomechat-user-pool
Pool Id us-east-1_Hnrx3Peoy
Pool ARN arn:aws:cognito-idp:us-east-1:607427101366:userpool/us-east-1_Hnrx3Peoy
App Client Id 7gnonc2rqinl49epft2jso4gg8

https://chat-app.auth.us-east-1.amazoncognito.com

aws cognito-idp sign-up \
  --region us-east-1 \
  --client-id 7gnonc2rqinl49epft2jso4gg8 \
  --username admin@example.com \
  --password Passw0rd!

aws cognito-idp admin-confirm-sign-up \
  --region us-east-1 \
  --user-pool-id us-east-1_Hnrx3Peoy \
  --username admin@example.com

Cognito User Pool policy
Awsomechat_execute_api
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "execute-api:*",
            "Resource": "*"
        }
    ]
}

Identity pool name

awsome chat app
Identity pool ID us-east-1:93f5afd5-2993-4ebe-917e-6133b48ea14f 