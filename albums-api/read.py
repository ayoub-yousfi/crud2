
import json
import boto3
import os
from boto3.dynamodb.conditions import Key
import simplejson as Json
def read(event,context):
    
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ALBUMS_TABLE')
    table = dynamodb.Table("crud-AlbumTable-1JB2TNM58ZYPM")
   # album_id = int(event ['pathParameters']['id'])
    #print(album_id)
   #response = table.get_item(Key={'AlbumId': album_id})
    response = table.scan()['Items']

    print(response)
    return{
       'statusCode':201,
     'headers': {
            'Content-Type': 'application/json',
        },
       'body': response
    }
    
    