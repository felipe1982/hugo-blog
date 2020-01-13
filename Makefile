STACK_NAME ?= hugo-blog
GITHUB_TOKEN_FILE ?= github-token.txt
SECRET_ID ?= github-token
AWS_DEFAULT_REGION ?= us-east-1

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
	--region $(AWS_DEFAULT_REGION)

update-github-token: $(GITHUB_TOKEN_FILE)
	aws secretsmanager put-secret-value \
	--secret-id "$(STACK_NAME)/$(SECRET_ID)" \
	--secret-string "file://$(GITHUB_TOKEN_FILE)" \
	--region $(AWS_DEFAULT_REGION)

all: create-stack update-stack wait-create-stack wait-update-stack deploy build-clean bucket sync

create-stack update-stack:
	aws cloudformation $@ \
	--stack-name $(STACK_NAME) \
	--capabilities CAPABILITY_IAM \
	--template-body file://cloudformation/hugo-codepipeline.yml \
	--parameters file://parameters.json \
	--region $(AWS_DEFAULT_REGION);
	$(MAKE) wait-$@

wait-create-stack:
	aws cloudformation wait stack-create-complete \
	--stack-name $(STACK_NAME)

wait-update-stack:
	aws cloudformation wait stack-update-complete --stack-name $(STACK_NAME)

build-clean:
	hugo --debug --verbose --cleanDestinationDir --destination public

deploy:
	aws --region us-east-1  \
	cloudformation update-stack --stack-name hugo-blog --capabilities CAPABILITY_IAM \
	--template-body file://cloudformation/hugo-codepipeline.yml \
	--parameters ParameterKey=GitHubUser,ParameterValue=felipe1982 \
	ParameterKey=OriginName,ParameterValue=com-felipe1982

sync:
	BUCKET=$$(aws cloudformation describe-stacks --stack-name hugo-blog --query 'Stacks[*].Outputs[?OutputKey==`Bucket`].OutputValue' --output text); \
	aws s3 sync --no-progress --storage-class STANDARD --delete --cache-control max-age=0 \
	public/ s3://$${BUCKET?} | tee aws-sync.log

.PHONY: all bucket sync create-stack update-stack create-github-token update-github-token
