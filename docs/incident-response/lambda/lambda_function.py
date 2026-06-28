import json
import boto3
import os

ec2 = boto3.client('ec2')

# Replace with your own Isolation Security Group ID, or set the
# ISOLATION_SG_ID environment variable on the Lambda function.
ISOLATION_SG_ID = os.environ.get('ISOLATION_SG_ID', 'sg-xxxxxxxxxxxxxxxxx')


def lambda_handler(event, context):
    print("Received GuardDuty Event:", json.dumps(event))

    try:
        finding_detail = event.get('detail', {})
        resource = finding_detail.get('resource', {})
        instance_details = resource.get('instanceDetails', {})
        instance_id = instance_details.get('instanceId')

        if not instance_id:
            return {'statusCode': 400, 'body': json.dumps('No Instance ID detected.')}

        # Override the existing security groups with ONLY the isolation group.
        response = ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[ISOLATION_SG_ID]
        )

        return {'statusCode': 200, 'body': json.dumps(f"Successfully isolated {instance_id}")}

    except Exception as e:
        raise e
