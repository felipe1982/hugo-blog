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

.PHONY: create-github-token
create-github-token: $(GITHUB_TOKEN_FILE)
	aws secretsmanager create-secret \
	--name "$(STACK_NAME)/$(SECRET_ID)" \
	--description "github token for $(STACK_NAME)" \
	--secret-string file://github-token.txt \
	--profile $(AWS_PROFILE) \
	--region $(AWS_DEFAULT_REGION)

.PHONY: update-github-token
update-github-token: $(GITHUB_TOKEN_FILE)
	aws secretsmanager put-secret-value \
	--secret-id "$(STACK_NAME)/$(SECRET_ID)" \
	--secret-string "file://$(GITHUB_TOKEN_FILE)" \
	--profile $(AWS_PROFILE) \
	--region $(AWS_DEFAULT_REGION)

.PHONY: create-stack update-stack
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
