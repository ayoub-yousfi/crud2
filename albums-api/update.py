import json
import boto3
import os

   
def update(event,context):
   print("hello")

   print(json.loads(event['body']))
   album = json.loads(event['body'])
   


   
   dynamodb = boto3.resource('dynamodb')
   table_name = os.environ.get('ALBUMS_TABLE')
   table = dynamodb.Table("crud-AlbumTable-1JB2TNM58ZYPM")
   #Verifier si l'albu se trouve deja ou nn 
   album_id = int(event ['pathParameters']['id'])
   #print(album_id)
   response = table.get_item(Key={'AlbumId': album_id})
   item = event['body']

   print(item)
   print("his")
   
   
   response = table.update_item(
        Key={
            'AlbumId': album_id
        },
      UpdateExpression="set AlbumName = :p",
      ExpressionAttributeValues={
      
      # decimal, Converts a finite Decimal instance to a rational number, exactly.
        ':p': album['AlbumName'],
        
    },
    ReturnValues="UPDATED_NEW"
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