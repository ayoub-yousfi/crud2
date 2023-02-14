import json
import boto3
import os
import uuid

   
def create(event,context):
   print("hello")

   print(json.loads(event['body']))
   album = json.loads(event['body'])
   params = {
        'AlbumId': album['AlbumId'],
        'AlbumName': album['AlbumName'],
        'DateRelease': album['DateRelease'],
        'ArtistId': album['ArtistId'],
        'GenreId': album['GenreId']
    }


   
   dynamodb = boto3.resource('dynamodb')
   table_name = os.environ.get('ALBUMS_TABLE')
   table = dynamodb.Table("crud-AlbumTable-1JB2TNM58ZYPM")
   response = table.put_item(
       TableName=table,
       
        Item=params
    )
   print(response)

 
  
  
   return{
       
       'statusCode': 200,
       'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
       'body': json.dumps({'message':response})
       
    
        
       
   }