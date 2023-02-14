import json
import boto3
import os
from boto3.dynamodb.conditions import Key
import simplejson as Json
def delete(event,context):
    
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ALBUMS_TABLE')
    table = dynamodb.Table("crud-AlbumTable-1JB2TNM58ZYPM")

    album_id = int(event ['pathParameters']['id'])
    print(album_id)
    response = table.delete_item(Key={'AlbumId': album_id})

    print(response)
    return{
       
       'statusCode': 200,
       'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
       'body': json.dumps({'message':"deleted"})
       
    
        
       
   }