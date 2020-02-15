#!/usr/bin/env python3
from crhelper import CfnResource
import boto3
route53_client = boto3.client("route53")
helper = CfnResource()

def resource_record_exists(HostedZoneId, StartRecordName, StartRecordType):
    response = route53_client.list_resource_record_sets(
        HostedZoneId=HostedZoneId,
        StartRecordName=StartRecordName,
        StartRecordType=StartRecordType,
        MaxItems='1'
    )
    return response['ResourceRecordSets'][0]['Name'] == StartRecordName
@helper.create
@helper.update
def create(event, context):
    HostedZoneId = event['ResourceProperties']['HostedZoneId']
    Name = event['ResourceProperties']['Name']
    Type = event['ResourceProperties']['Type']
    Value = event['ResourceProperties']['Value']
    response = route53_client.change_resource_record_sets(
        HostedZoneId=HostedZoneId,
        ChangeBatch={
            'Changes': [
                {
                    'Action':'UPSERT',
                    'ResourceRecordSet': {
                        'Name': Name,
                        'Type': Type,
                        'TTL': 86400,
                        'ResourceRecords': [
                            {
                                'Value': Value
                            }
                        ]
                    }
                }
            ]
        }
    )
    return response
@helper.delete
def delete_record(event, context):
    HostedZoneId = event['ResourceProperties']['HostedZoneId']
    Name = event['ResourceProperties']['Name']
    Type = event['ResourceProperties']['Type']
    Value = event['ResourceProperties']['Value']
    if not resource_record_exists(HostedZoneId, Name, Type):
        return None
    route53_client.change_resource_record_sets(
        HostedZoneId=HostedZoneId,
        ChangeBatch={
            'Changes': [
                {
                    'Action':'DELETE',
                    'ResourceRecordSet': {
                        'Name': Name,
                        'Type': Type,
                        'TTL': 86400,
                        'ResourceRecords': [
                            {
                                'Value': Value
                            }
                        ]
                    }
                }
            ]
        }
    )
    return None

def handler(event, context):
    HostedZoneId = event['ResourceProperties']['HostedZoneId']
    Name = event['ResourceProperties']['Name']
    Type = event['ResourceProperties']['Type']
    Value = event['ResourceProperties']['Value']
    helper(event, context)
