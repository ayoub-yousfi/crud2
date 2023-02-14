version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "albumss"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-8eupftz8ihgd"
s3_prefix = "albumss"
region = "eu-west-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = []

[Y]
[Y.deploy]
[Y.deploy.parameters]
stack_name = "albapi"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-8eupftz8ihgd"
s3_prefix = "albapi"
region = "eu-west-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = []

[default]
[default.deploy]
[default.deploy.parameters]
stack_name = "albapi"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-8eupftz8ihgd"
s3_prefix = "albapi"
region = "eu-west-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = []
