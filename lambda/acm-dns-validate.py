#!/usr/bin/env python3
from crhelper import CfnResource
import boto3

NAME = 'boto3.felipe1982.com.'
TYPE = 'CNAME'
VALUE = '192.0.2.100'
HOSTEDZONEID = 'Z1JYG3XEZZ05O1'
route53_client = boto3.client("route53")
def resource_record_exists(route53_client, HostedZoneId, StartRecordName=None, StartRecordType=None):
    try:
        response = route53_client.list_resource_record_sets(
            HostedZoneId=HostedZoneId,
            StartRecordName=StartRecordName,
            StartRecordType=StartRecordType,
            MaxItems='1'
        )
    except:
        raise
    return response['ResourceRecordSets'][0]['Name'] == StartRecordName
def upsert_record(route53_client, hostedzoneid, name, type, value):
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=hostedzoneid,
            ChangeBatch={
                'Changes': [
                    {
                        'Action':'UPSERT',
                        'ResourceRecordSet': {
                            'Name': name,
                            'Type': type,
                            'TTL': 86400,
                            'ResourceRecords': [
                                {
                                    'Value': value
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

def delete_record(route53_client, hostedzoneid, name, type, value):
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=hostedzoneid,
            ChangeBatch={
                'Changes': [
                    {
                        'Action':'DELETE',
                        'ResourceRecordSet': {
                            'Name': name,
                            'Type': type,
                            'TTL': 86400,
                            'ResourceRecords': [
                                {
                                    'Value': value
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
upsert_record(route53_client, HOSTEDZONEID, NAME, TYPE, VALUE)

if resource_record_exists(route53_client, HOSTEDZONEID, NAME, TYPE):
    print(f"Hooray! {NAME} exists")
    delete_record(route53_client, HOSTEDZONEID, NAME, TYPE, VALUE)
    if not resource_record_exists(route53_client, HOSTEDZONEID, NAME, TYPE):
        print(f"{NAME} was deleted from HostedZoneId {HOSTEDZONEID}")
else:
    print(f"{NAME} does not exist")
# # what do I need?

# - hosted zone name (or hosted zone id)
# - zone DNS name (example.com)
# - Resource Record to add (xyz.example.com)
# - CNAME to point to (xyz.acm-validation.aws)
# - certificate ARN
#   - name
#   - value
#   - type of domain for TLS certificate
