STACK_NAME ?= hugo-blog
AWS_PROFILE ?= myuser
GITHUB_TOKEN_FILE ?= github-token.txt
SECRET_ID ?= github-token

$(GITHUB_TOKEN_FILE):
	@echo "Creating secrets file '$(GITHUB_TOKEN_FILE)'"
	TEMPFILE=$$(mktemp); \
	TOKEN=red; \
	read -s -r -p "Please paste your GitHub Personal Access Token: " TOKEN; echo; \
	cat > $$TEMPFILE <<<$$TOKEN; \
	install -o $$(id -nu) -g $$(id -ng) -m 600 $$TEMPFILE $(GITHUB_TOKEN_FILE)

create-github-token: $(GITHUB_TOKEN_FILE)
	aws secretsmanager create-secret \
	--name "$(STACK_NAME)/$(SECRET_ID)" \
	--description "github token for $(STACK_NAME)" \
	--secret-string file://github-token.txt \
	--profile $(AWS_PROFILE) \
	--region $(AWS_DEFAULT_REGION)

update-github-token: $(GITHUB_TOKEN_FILE)
	aws secretsmanager put-secret-value \
	--secret-id "$(STACK_NAME)/$(SECRET_ID)" \
	--secret-string "file://$(GITHUB_TOKEN_FILE)" \
	--profile $(AWS_PROFILE) \
	--region $(AWS_DEFAULT_REGION)

create-stack update-stack:
	aws cloudformation $@ \
	--stack-name $(STACK_NAME) \
	--capabilities CAPABILITY_IAM \
	--template-body file://cloudformation/hugo-codepipeline.yml \
	--parameters file://parameters.json \
	--profile $(AWS_PROFILE) \
	--region $(AWS_DEFAULT_REGION)

build-clean:
	hugo --verbose --cleanDestinationDir --destination public

deploy:
	aws --region us-east-1 --profile myuser \
	cloudformation update-stack --stack-name hugo-blog --capabilities CAPABILITY_IAM \
	--template-body file://cloudformation/hugo-codepipeline.yml \
	--parameters ParameterKey=GitHubUser,ParameterValue=felipe1982 \
	ParameterKey=OriginName,ParameterValue=com-felipe1982

bucket:
$(eval BUCKET=$(shell aws --profile myuser cloudformation describe-stacks  --stack-name hugo-blog --query 'Stacks[*].Outputs[?OutputKey==`Bucket`].OutputValue' --output text))

sync: bucket
	aws --profile myuser s3 sync --no-progress --storage-class STANDARD_IA --delete public/ s3://$(BUCKET)

all: deploy build-clean bucket sync

.PHONY: all bucket sync create-stack update-stack create-github-token update-github-token
