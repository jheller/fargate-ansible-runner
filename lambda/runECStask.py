import sys
import logging
import boto3
import json
import os

logger = logging.getLogger()
logger.setLevel('INFO')

def lambdaHandler(event, context):
    logger.info("event: %s" % json.dumps(event))

    detail = event['detail']
    subnetA = os.environ.get("SUBNET_A")
    subnetB = os.environ.get("SUBNET_B")
    subnetC = os.environ.get("SUBNET_C")
    securityGroup = os.environ.get("SECURITY_GROUP")

    ecs = boto3.client('ecs')

    network = {
        'awsvpcConfiguration': {
            'subnets': [
                subnetA,
                subnetB,
                subnetC
            ],
            'securityGroups': [
                securityGroup
            ],
            'assignPublicIp': 'DISABLED'
        }
    }

    overrides = {
        'containerOverrides': [
            {
                'name': 'ansible-runner',
                'environment': [
                    {
                        'name': 'Playbook',
                        'value': os.environ.get("Playbook")
                    },
                    {
                        'name': 'ASG_NAME',
                        'value': detail['AutoScalingGroupName']
                    },
                    {
                        'name': 'HOOK_NAME',
                        'value': detail['LifecycleHookName']
                    },
                    {
                        'name': 'ACTION_TOKEN',
                        'value': detail['LifecycleActionToken']
                    },
                ]
            }
        ]
    }

    response = ecs.run_task(
        cluster = os.environ.get("CLUSTER"),
        taskDefinition='ansible-runner',
        launchType='FARGATE',
        networkConfiguration=network,
        overrides=overrides
    )

    # Output an indication of the running task
    if len(response['tasks']) > 0:
        for container in response['tasks'][0]['containers']:
            logger.info(f"Name: {container['name']}")
            logger.info(f"Image: {container['image']}")
            logger.info(f"Status: {container['lastStatus']}")
    else:
        logger.info("No tasks started")
