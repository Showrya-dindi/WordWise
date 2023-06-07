import googleapiclient.discovery
import boto3
import json

def lambda_handler(event, context):
    try:
        
        #Enter you gcloud developer key
        developer_key = "YOUR_DEVELOPER_KEY"
        api_service_name = "youtube"
        api_version = "v3"
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = developer_key)
        s3 = boto3.client('s3')

        #Enter the video id eg: https://www.youtube.com/watch?v=UwsrzCVZAb8
        video_id = "UwsrzCVZAb8"
        #Maximum no. of pages to be loaded
        max_pages = 3

        #Loop to load each page as json document into s3 bucket
        for i in range(max_pages):
            if i == 0:
                request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId=video_id,
                    textFormat="textFormatUnspecified"
                )
            else:
                request = youtube.commentThreads().list(
                    part="snippet,replies",
                    pageToken=page_token,
                    videoId=video_id,
                    textFormat="textFormatUnspecified"
                )
            
            response = request.execute()
            
            json_file = json.dumps(response['items']).encode('UTF-8')
            s3.put_object(
            Body=json_file,
            Bucket='YOUR_BUCKET_NAME',
            Key=f'file_{i}.json'
            )

            if 'nextPageToken' in response:
                page_token=response['nextPageToken']
            else:
                break
        
        return {'statusCode': 200,'body': json.dumps('Successful!!')}
    except Exception as e:
        return {'Failed': e}
