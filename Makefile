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

all: validate-template create-stack update-stack wait-create-stack wait-update-stack build-clean hugo bucket sync

validate-template:
	aws cloudformation validate-template --template-body file://cloudformation/hugo-codepipeline.yml

create-stack update-stack: validate-template
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

build-clean hugo:
	hugo --debug --verbose --cleanDestinationDir --destination public | tee hugo-build.log

sync:
	BUCKET=$$(aws cloudformation describe-stacks --stack-name hugo-blog --query 'Stacks[*].Outputs[?OutputKey==`Bucket`].OutputValue' --output text); \
	aws s3 sync --no-progress --storage-class STANDARD --delete --cache-control max-age=0 \
	public/ s3://$${BUCKET?} | tee aws-sync.log

.PHONY: all bucket sync create-stack update-stack create-github-token update-github-token
