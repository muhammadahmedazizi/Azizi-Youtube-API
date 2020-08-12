from secret import api_key
from apiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=api_key)
req = youtube.search().list(q='indian pythonista', part='snippet', type='channel', maxResults=50)
res = req.execute()
#print (len(res))

for item in res['items']:
    print (item['snippet'])

