STACK_NAME ?= hugo-blog
GITHUB_TOKEN_FILE ?= github-token.txt
SECRET_ID ?= github-token
AWS_DEFAULT_REGION ?= us-east-1
TEMPLATE_DIR := cloudformation
TEMPLATE := lambda-functions.yml
TEMPLATE_OUTPUT := packaged_$(TEMPLATE)

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

server:
	hugo server --debug --verbose

bucket:
	@echo 'Call    eval `make bucket`' >&2
	@echo export S3_WEBSITE_BUCKET="$$(aws cloudformation describe-stacks --stack-name hugo-blog --query 'Stacks[*].Outputs[?OutputKey==`Bucket`].OutputValue' --output text)"

sync:
	# export S3_WEBSITE_BUCKET
	aws s3 sync --no-progress --storage-class STANDARD --delete --cache-control max-age=0 \
	public/ s3://$${S3_WEBSITE_BUCKET?} | tee aws-sync.log

lambda: clean package lint deploy

package $(TEMPLATE_OUTPUT):
	aws cloudformation package --template-file $(TEMPLATE_DIR)/$(TEMPLATE)  --output-template-file $(TEMPLATE_OUTPUT) --s3-bucket cfn-638088845137-us-east-1
lint: $(TEMPLATE_OUTPUT)
	cfn-lint --info --template $(TEMPLATE_OUTPUT)
deploy: $(TEMPLATE_OUTPUT)
	aws cloudformation deploy --template-file $(TEMPLATE_OUTPUT) --stack-name $(LAMBDA_STACK_NAME) --capabilities CAPABILITY_IAM
clean:
	-rm $(TEMPLATE_OUTPUT)
delete:
	aws cloudformation delete-stack --stack-name $(LAMBDA_STACK_NAME)
.PHONY: all build-clean hugo bucket sync server create-stack \
	update-stack wait-create-stack wait-update-stack \
	validate-template create-github-token update-github-token \
	lint clean delete
