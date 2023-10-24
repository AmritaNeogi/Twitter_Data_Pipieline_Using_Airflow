from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import s3fs


def run_yt_etl():

    api_key = ' '

    # based on the youtube service we can request the api for the data we require
    # provided by google
    api_service_name = "youtube"
    api_version = "v3"
    youtube_service = build(api_service_name, api_version, developerKey= api_key)
    # Read the CSV and iterate through channel IDs
    df = pd.read_csv("/Youtube_channel_ids/channel_ids.csv")
    # Select the first 50 records from the DataFrame since the API key would allow only that many
    records = df.head(50)

    # Extract the channel IDs from the selected records
    channel_ids = records.iloc[:, 1].tolist()
    #print(channel_ids)

    # # Extract the channel details/statistics
    def get_channel_stats(youtube_service, channel_ids):
        result =[]
        request= youtube_service.channels().list(
            part= 'snippet,contentDetails,statistics',
            id = channel_ids)
        response = request.execute()
        for i in range (len(response['items'])):
            data = dict(Channel_Name = response['items'][i]['snippet']['title'],
                    Description = response['items'][i]['snippet']['description'],
                    Published_Date = response['items'][i]['snippet']['publishedAt'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Videos = response['items'][i]['statistics']['videoCount']
                    )
            result.append(data)
        return result

    result_df = get_channel_stats(youtube_service, channel_ids)
    channel_stat = pd.DataFrame(result_df)

    #  Save the extracted data to a new CSV file
    # channel_stat.to_csv('youtube_stat.csv', index=False) 
    channel_stat.to_csv('s3://amrita-neogi-yt-bucket/youtube_stat.csv') # Replace with  desired S3 path and filename
