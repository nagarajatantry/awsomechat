

Built following online guide: [Serverless Stack](https://serverless-stack.com/#table-of-contents)

Logged in to AWS console under HearRo account

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



IAM user serverless01
Using custom JSON access policy: serverless_backend
``` json
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "cloudformation:*",
            "s3:*",
            "logs:*",
            "iam:*",
            "apigateway:*",
            "lambda:*",
            "ec2:DescribeSecurityGroups",
            "ec2:DescribeSubnets",
            "ec2:DescribeVpcs",
            "events:*"
        ],
        "Resource": [
            "*"
        ]
        }
    ]
    }
```
---
User name: `serverless01`  
AWS access type: `Programmatic access - with an access key`

**Permissions summary**  
The following policies will be attached to the user shown above.

Type: `Managed policy`  
Name: `serverless_backend`

access key ID: `see LastPass`  
secret access key: `see LastPass`

DynamoDB table name: `serverless01`

```ini
Table name serverless01
Primary partition key userId (String)
Primary sort key noteId (String)
Point-in-time recovery DISABLED  
Enable Encryption DISABLED
Time to live attribute DISABLED  
Manage TTL Table status Active
Creation date April 12, 2018 at 4:08:44 PM UTC-7
UTC: April 12, 2018 at 11:08:44 PM UTC
Local: April 12, 2018 at 4:08:44 PM UTC-7
Region (Ohio): April 12, 2018 at 6:08:44 PM UTC-5
Provisioned read capacity units 5 (Auto Scaling Enabled)
Provisioned write capacity units 5 (Auto Scaling Enabled)
Last decrease time -
Last increase time -
Storage size (in bytes) 0 bytes
Item count 0
Region US East (Ohio)
Amazon Resource Name (ARN) arn:aws:dynamodb:us-east-2:191109976016:table/serverless01

```

S3 Bucket for uploads
    Bucket name hro-app-uploads	
    Region US East (Ohio)

```cli
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>

```

Cognito User Pool name: `hro-app-user-pool`
Pool Id `us-east-2_IrZXJOwJB`
Pool ARN `arn:aws:cognito-idp:us-east-2:191109976016:userpool/us-east-2_IrZXJOwJB`

App Client name: `hro-app`
App client id: `334n0k698qhsi18u9n3g9l0hte`
Domain name: `https://hro-app.auth.us-east-2.amazoncognito.com`

Setup test user account

```
aws cognito-idp sign-up \
  --region us-east-2 \
  --client-id 334n0k698qhsi18u9n3g9l0hte \
  --username test2@example.com \
  --password Passw0rd!

```

Verify account

```
  aws cognito-idp admin-confirm-sign-up \
  --region us-east-2 \
  --user-pool-id us-east-2_IrZXJOwJB \
  --username test2@example.com

```

`serverless install --url https://github.com/AnomalyInnovations/serverless-nodejs-starter --name hro-app-api`

serverless.yml

```yml
    service: hro-app-api

    # Use the serverless-webpack plugin to transpile ES6
    plugins:
    - serverless-webpack
    - serverless-offline

    # serverless-webpack configuration
    # Enable auto-packing of external modules
    custom:
    webpack:
        webpackConfig: ./webpack.config.js
        includeModules: true

    provider:
    name: aws
    runtime: nodejs8.10
    stage: prod
    region: us-east-2
```

`\"noteId\":\"6b28e370-3eb3-11e8-97f4-dd5a47fb034e\" 02727ed0-3eb9-11e8-9d78-ff45080619b6`

`8c8616c0-4686-11e8-b3ca-fd34abc86844`
"body": "{\"userId\":\"USER-SUB-1234\",\"noteId\":\"8c8616c0-4686-11e8-b3ca-fd34abc86844\",\"content\":\"hello world\",\"attachment\":\"hello.jpg\",\"createdAt\":1524440433199}"

```
Service Information
service: hro-app-api
stage: prod
region: us-east-2
stack: hro-app-api-prod
api keys:
  None
endpoints:
  POST - https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/notes
  GET - https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/notes/{id}
  GET - https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/notes
  PUT - https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/notes/{id}
  DELETE - https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/notes/{id}
functions:
  create: hro-app-api-prod-create
  get: hro-app-api-prod-get
  list: hro-app-api-prod-list
  update: hro-app-api-prod-update
  delete: hro-app-api-prod-delete
  ```

https://serverless-stack.com/chapters/create-a-cognito-identity-pool.html


```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "mobileanalytics:PutEvents",
        "cognito-sync:*",
        "cognito-identity:*"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::hro-app-uploads/private/${cognito-identity.amazonaws.com:sub}/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "execute-api:Invoke"
      ],
      "Resource": [
        "arn:aws:execute-api:us-east-2:*:nhvdsgcnkl/*"
      ]
    }
  ]
}
```

Identity pool name `hro_app_01`  
Identity pool ID `us-east-2:86bfd12f-910a-4bb6-b74a-aced297b44f8`


```bash
npx aws-api-gateway-cli-test \
--username='test2@example.com' \
--password='Passw0rd!' \
--user-pool-id='us-east-2_IrZXJOwJB' \
--app-client-id='334n0k698qhsi18u9n3g9l0hte' \
--cognito-region='us-east-2' \
--identity-pool-id='us-east-2:86bfd12f-910a-4bb6-b74a-aced297b44f8' \
--invoke-url='https://nhvdsgcnkl.execute-api.us-east-2.amazonaws.com/prod/' \
--api-gateway-region='us-east-2' \
--path-template='notes' \
--method='POST' \
--body='{"content":"hello world","attachment":"hello.jpg"}'

```

**Create a New React.js App**  
https://serverless-stack.com/chapters/create-a-new-reactjs-app.html

`npx create-react-app hro-app-client`