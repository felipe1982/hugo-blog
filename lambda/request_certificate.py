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
def request_certificate(DomainName, SubjectAlternativeNames=None):
    if SubjectAlternativeNames:
        response = acm_client.request_certificate(
            DomainName=DomainName,
            SubjectAlternativeNames=SubjectAlternativeNames,
            ValidationMethod='DNS'
        )
    else:
        response = acm_client.request_certificate(
            DomainName=DomainName,
            ValidationMethod='DNS'
        )
    return {"Arn" : response['CertificateArn']}
def handler(event, context):
    helper(event, context)
