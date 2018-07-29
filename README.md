AWS programatic user
awsomechat
Access key ID AKIAI3S6IK4H5QUWRC5Q
Secret access key 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

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