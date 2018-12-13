# http://felipe1982.com

### Felipe's personal blog on S3

Using [Hugo]

http://felipe1982.com

[Hugo]:https://gohugo.io

1.  `make github-token.txt`
This creates a `0600` mode text file with your GitHub Personal Access Token

2.  `make create-github-token`
Create (empty) secret in AWS Secrets Manager

3.  `make update-github-token`
Put (overwrite) secret

4.  `make create-stack`
Create CloudFormation stack

5.  `make update-stack`
Update CloudFormation stack
