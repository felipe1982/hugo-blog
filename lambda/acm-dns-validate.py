#!/usr/bin/env python3
from crhelper import CfnResource
import logging
import boto3

logger = logging.getLogger(__name__)

# NAME = 'boto3.felipe1982.com.'
# TYPE = 'CNAME'
# VALUE = '192.0.2.100'
# HOSTEDZONEID = 'Z1JYG3XEZZ05O1'
helper = CfnResource()
try:
    route53_client = boto3.client("route53")
except Exception as e:
    helper.init_failure(e)

def resource_record_exists(event, context):
    try:
        response = route53_client.list_resource_record_sets(
            HostedZoneId=event['ResourceProperties']['HostedZoneId'],
            StartRecordName=event['ResourceProperties']['Name'],
            StartRecordType=event['ResourceProperties']['Type'],
            MaxItems='1'
        )
    except:
        raise
    return response['ResourceRecordSets'][0]['Name'] == event['ResourceProperties']['Name']
# @helper.create
def create(event, context):
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=event['ResourceProperties']['HostedZoneId'],
            ChangeBatch={
                'Changes': [
                    {
                        'Action':'UPSERT',
                        'ResourceRecordSet': {
                            'Name': event['ResourceProperties']['Name'],
                            'Type': event['ResourceProperties']['Type'],
                            'TTL': 86400,
                            'ResourceRecords': [
                                {
                                    'Value': event['ResourceProperties']['Value']
                                }
                            ]
                        }
                    }
                ]
            }
        )
    except:
        raise
    return response
# @helper.delete
def delete_record(event, context):
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=event['ResourceProperties']['HostedZoneId'],
            ChangeBatch={
                'Changes': [
                    {
                        'Action':'DELETE',
                        'ResourceRecordSet': {
                            'Name': event['ResourceProperties']['Name'],
                            'Type': event['ResourceProperties']['Type'],
                            'TTL': 86400,
                            'ResourceRecords': [
                                {
                                    'Value': event['ResourceProperties']['Value']
                                }
                            ]
                        }
                    }
                ]
            }
        )
    except:
        raise
    return response

def handler(event, context):
    # helper(event, context)
    create(event, context)

    if resource_record_exists(event, context):
        print(f"Hooray! {NAME} exists")
        delete_record(event, context)
        if not resource_record_exists(event, context):
            print(f"{NAME} was deleted from HostedZoneId {HOSTEDZONEID}")
    else:
        print(f"{NAME} does not exist")

if __name__ == '__main__':
    event = {
        "RequestType" : "Create",
        "ResponseURL" : "http://pre-signed-S3-url-for-response",
        "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/stack-name/guid",
        "RequestId" : "unique id for this create request",
        "ResourceType" : "Custom::TestResource",
        "LogicalResourceId" : "MyTestResource",
        "ResourceProperties" : {
            "HostedZoneId" : "Z1JYG3XEZZ05O1",
            "Name" : "boto3.felipe1982.com",
            "Type" : "CNAME",
            "Value" : "aws.amazon.com"
        }
    }
    context = None
    handler(event, context)
