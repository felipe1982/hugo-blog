#!/usr/bin/env python3
import boto3
acm_client = boto3.client('acm')

def request_certificate(DomainName, SubjectAlternativeNames):
    response = acm_client.request_certificate(
        DomainName=DomainName,
        SubjectAlternativeNames=SubjectAlternativeNames,
        ValidationMethod='DNS'
    )
    return response['CertificateArn']
