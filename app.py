#-*- coding: utf-8 -*-

import json
import requests

import logging
import boto3
from botocore.exceptions import ClientError
import os
import requests
import time


local_path = "/tmp/temp_file" #"/mnt/test/tmp"


def get_file(url):
    r = requests.get(url)
    with open(local_path, 'wb') as f:
        f.write(r.content) 

def rm_file(file_path):
    os.remove(file_path)


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def lambda_handler(event, context):
    url = event['url']
    bucket = event['bucket']
    prefix = event['prefix']+'/'+url.split('/')[-1]
    s3path='s3://'+bucket+'/'+prefix
    get_file(url)
    upload_file(local_path, bucket, prefix)
    time.sleep(1)
    rm_file(local_path)
    responseObject ={}
    responseObject['statusCode'] = 200
    responseObject['headers']= {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['headers']['s3path'] = s3path
    
    return responseObject