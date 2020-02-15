#!/usr/bin/env python3
import boto3
from crhelper import CfnResource
acm_client = boto3.client('acm')
helper = CfnResource()
@helper.create
def create(event, context):
    DomainName = event['ResourceProperties']['DomainName']
    SubjectAlternativeNames = event['ResourceProperties'].get('SubjectAlternativeNames', None)
    CertificateArn = request_certificate(DomainName, SubjectAlternativeNames)
    helper.Data.update(CertificateArn)
    return None
def request_certificate(DomainName, SubjectAlternativeNames=None):
    if SubjectAlternativeNames:
        response = acm_client.request_certificate(
            DomainName=DomainName,
            ValidationMethod='DNS',
            SubjectAlternativeNames=SubjectAlternativeNames,
            IdempotencyToken=DomainName.replace('.','')
        )
    else:
        response = acm_client.request_certificate(
            DomainName=DomainName,
            ValidationMethod='DNS',
            IdempotencyToken=DomainName.replace('.','')
        )
    return {"Arn" : response['CertificateArn']}
@helper.delete
@helper.update
def noop(event, context):
    return None
def handler(event, context):
    helper(event, context)
