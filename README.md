# Ansible with Fargate Demo Using CodePipeline and CodeBuild

This demonstrates how to use CodePipeline to build docker images and push them to ECR.

The demo uses creates a Docker image based on [ansible-runner](https://github.com/ansible/ansible-runner) and includes Ansible playbooks to
manage web server instances. It demonstrates how this can be used to manage EC2 Autoscale instances
with Ansible.

Included here are:
* Dockerfile to create the docker image
* Ansible playbooks for a simple Apache web server (**project** folder)
* CloudFormation templates to create a CodePipeline and set up the demo webservers
managed by the Ansible playbooks. (**cloudformation** folder)

## Setup
The steps must be done in this order.

1. Create a CodeCommit repo in your AWS account called **fargate-ansible-runner** and push this repo to it.
1. Create an ECR repository called **fargate-ansible-runner**. This will hold the container images.
1. In the AWS console
    * Create an SSH key called **fargate-ansible-runner** and download the private key.
    * Create an SSM Parameter called **/ec2_key/fargate-ansible-runner** of type SecureString and place the contents of the private key file in it.
1. Create the VPC using the CloudFormation template **vpc.yml**.
1. Create the Load Balancers and Autoscaling group using the CloudFormation template **server_asg.yml**.
1. Create the CodePipeline the CloudFormation template **pipeline.yml**.

## Repo Contents

* [cloudformation](./cloudformation) folder contains cloudformation templates.
* **env** folder is copied into the docker container image.
* [project](./project) folder contains the Ansible project to be installed on the ansible-runner container.
* [lambda](./lambda) folder contains the source for the lambda function, but this is also embedded in the runner.yml template and it is deployed from there.
* **buildspec.yml** is used by CodeBuild to build the container and push it to ECR.
* **Dockerfile** is used to build the container image.
* **runner_entry.sh** is copied into the container image. It is run when the container starts.

## Operation
Changes can be made to the Ansible playbooks in the [project](./project) folder. When commits are made to the CodeCommit repo the pipeline will be triggered automatically to build the container image, push it to ECR and create or update an ECS Task Definition for it called **ansible-runner**.

On the autoscaling group for the web servers a lifecycle hook has been created with an EventBridge rule to trigger the Lambda function. The functiion will run the fargate-ansible-runner task as a Fargate container.

**Note**: Although EventBridge rules can trigger running an ECS Task directly, a Lambda intermediary is necessary to extract some information from the lifecycle event and make it available as environment variables to the ECS Task.
