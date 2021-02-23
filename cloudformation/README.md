# cloudformation
This folder contains CloudFormation templates used to set up the demo and to
deploy docker images to ECR.

| Template            | Description |
|---------------------|-------------|
| pipeline.yml        | Create a pipeline using CodePipeline and CodeBuild |
| runner.yml          | Used by CodePipeline to deploy an ECS Task definition and a Lambda function to run a Task |
| server_asg.yml      | Creates a simple Load Balance and EC2 Autoscaling group for the demo. These are placed in the VPC. |
| vpc.yml             | Creates a simple VPC with public and private subnets and a NAT Gateway |
