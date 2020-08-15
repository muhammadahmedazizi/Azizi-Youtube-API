
from datetime import datetime
from secret import api_key
from apiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=api_key)

start_time = datetime(year=2005, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2007, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')

# Where 'q' is Search Query
req = youtube.search().list(q='iftikhar+arif',
                            part='snippet',
                            type='video',
                            maxResults=50,
                            publishedAfter=start_time,
                            publishedBefore=end_time)
res = req.execute()

for item in sorted(res['items'], key=lambda x:x['snippet']['publishedAt']):
    print(item['snippet']['title'],"|", item['snippet']['publishedAt'], item['id']['videoId'] )

