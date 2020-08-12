
from secret import api_key
from apiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=api_key)
req = youtube.search().list(q='Pink Panther', part='snippet', type='video', maxResults=50)
res = req.execute()
#print (len(res))

#Get a list of titles against your query
for item in res['items']:
    print (item['snippet']['title'])



