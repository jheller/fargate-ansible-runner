#!/usr/bin/env bash

cat <<EOF > /runner/env/extravars
---
RegionName: ${RegionName}
Platform: ${Platform}
TargetVpc: ${TargetVpc}
Site: ${Site}
version: ${version}
EOF

aws ssm get-parameter --name ${Ec2KeySSM} --with-decryption --region ${AWSregion} --output text --query 'Parameter.Value' >> /runner/env/ssh_key

# pass control to the base image entrypoint
exec entrypoint ansible-runner -p ${Playbook} run /runner
