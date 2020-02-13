#!/usr/bin/env python3
from crhelper import CfnResource
import boto3
acm_client = boto3.client('acm')
helper = CfnResource()

def get_certificate_cname_list(CertificateArn, DomainName):
    response = acm_client.describe_certificate(CertificateArn=CertificateArn)
    cname_dict = {}
    for resource_record in response['Certificate']['DomainValidationOptions']:
        if resource_record['DomainName'] == DomainName:
            cname_dict['Name'] = resource_record['ResourceRecord']['Name']
            cname_dict['Type'] = resource_record['ResourceRecord']['Type']
            cname_dict['Value'] = resource_record['ResourceRecord']['Value']
    return cname_dict

@helper.create
def create(event,context):
    CertificateArn = event['ResourceProperties']['CertificateArn']
    DomainName = event['ResourceProperties']['DomainName']
    cname_dict = get_certificate_cname_list(CertificateArn, DomainName)
    helper.Data.update(cname_dict)
    return None

@helper.delete
def noop(event, context):
    pass

def handler(event, context):
    helper(event, context)

if __name__ == '__main__':
    print(get_certificate_cname_list('arn:aws:acm:us-east-1:638088845137:certificate/def5f55f-13b6-49dd-9d85-477d19f275ef', 'www.felipe1982.com'))
