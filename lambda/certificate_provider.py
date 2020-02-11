#!/usr/bin/env python3
import boto3
from pprint import pprint

acm_client = boto3.client('acm')

def request_certificate(DomainName, SubjectAlternativeNames):
    response = acm_client.request_certificate(
        DomainName=DomainName,
        SubjectAlternativeNames=SubjectAlternativeNames,
        ValidationMethod='DNS'
    )
    return response['CertificateArn']

def get_certificate_cname_value(CertificateArn):
    response = acm_client.describe_certificate(
        CertificateArn=CertificateArn
    )
    cname_list = [ (resource_record['ResourceRecord']['Name'], resource_record['ResourceRecord']['Type'], resource_record['ResourceRecord']['Value']) for resource_record in response['Certificate']['DomainValidationOptions'] ]

    return cname_list

pprint(get_certificate_cname_value('arn:aws:acm:us-east-1:638088845137:certificate/def5f55f-13b6-49dd-9d85-477d19f275ef'))
