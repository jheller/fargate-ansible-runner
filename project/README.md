# Ansible Playbooks

This folder contains Ansible playbooks for configuring and maintaining EC2 instances.

It uses dynamic inventory to discover instances based on tags.

| Playbook            | Description                                 |
|---------------------|---------------------------------------------|
| site.yml            | Sample Apache install                       |
| lifecycle.yml       | Apache install + ASG lifecycle notification |
