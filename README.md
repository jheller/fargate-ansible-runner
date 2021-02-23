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
1. Create the VPC using **vpc.yml**.
1. Create the Load Balancers and Autoscaling group using **server_asg.yml**.
1. Create the CodePipeline using the pipeline.yml template. The parameters specify the CodeCommit repo and ECR.

## Contents

* [cloudformation](./cloudformation) contains cloudformation templates
* **env** folder is copied into the docker container image
* [project](./project) contains the Ansible project to be installed on the ansible-runner container.
* [lambda](./lambda) contains the source for the lambda function, but this is also embedded in the runner.yml template.
* **buildspec.yml** is used by CodeBuild to build the container and push it to ECR.
* **Dockerfile** is used to build the container image
* **runner_entry.sh** is copied into the container image. It is run when the container starts.
