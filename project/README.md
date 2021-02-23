# Ansible Playbooks

This folder contains the Ansible playbooks for configuring and maintaining EC2 instances.

| Playbook            | Description                                 |
|---------------------|---------------------------------------------|
| site.yml            | Runs just the apache role                   |
| lifecycle.yml       | Runs the apache and asg_lifecycle roles.    |

## Roles
| Role             | Description                                 |
|------------------|---------------------------------------------|
| apache           | Simple Apache install with a templated index.html |
| asg_lifecycle    | ASG complete-lifecycle notification               |

## Inventory
The [aws_ec2](https://docs.ansible.com/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html) inventory plugin
is used. This dynamically finds EC2 target hosts using defined filters. In this case it is looking for instances with the tag **ansible-target** set to 'apache'.
