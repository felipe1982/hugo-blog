#!/usr/bin/env python3
from crhelper import CfnResource
import boto3
import re
import time

NAME = 'boto3.felipe1982.com.'
TYPE = 'A'
VALUE = '192.0.2.100'
HOSTEDZONEID = 'Z1JYG3XEZZ05O1'
route53_client = boto3.client("route53")
def upsert_record(route53_client, hostedzoneid, name, type, value):
    route53_client.change_resource_record_sets(
        HostedZoneId=hostedzoneid,
        ChangeBatch={
            'Changes': [
                {
                    'Action':'UPSERT',
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': type,
                        'TTL': 300,
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
def delete_record(route53_client, hostedzoneid, name, type, value):
    route53_client.change_resource_record_sets(
        HostedZoneId=hostedzoneid,
        ChangeBatch={
            'Changes': [
                {
                    'Action':'DELETE',
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': type,
                        'TTL': 300,
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
delete_record(route53_client, HOSTEDZONEID, NAME, TYPE, VALUE)
upsert_record(route53_client, HOSTEDZONEID, NAME, TYPE, VALUE)

def get_zone_id_from_name(zone_name):
    pass
def upsert_dns_resource_record(route53_client, zone_id, name, value):
    pass
def get_cname_from_cert():
    pass

def handler(event, context):
    print("printing event")
    print(event)
    print("printing contenxt")
    print(context)


# # what do I need?

# - hosted zone name (or hosted zone id)
# - zone DNS name (example.com)
# - Resource Record to add (xyz.example.com)
# - CNAME to point to (xyz.acm-validation.aws)
# - certificate ARN
#   - name
#   - value
#   - type of domain for TLS certificate
