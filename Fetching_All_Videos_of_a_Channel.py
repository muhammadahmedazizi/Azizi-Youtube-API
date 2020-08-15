
from datetime import datetime
from secret import api_key
from apiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=api_key)


#res = youtube.channels().list(id='UCkUq-s6z57uJFUFBvZIVTyg',part='contentDetails').execute()
#res = youtube.playlistitems().list

def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()

    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos  = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken = next_page_token,
                                           ).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    for num, video in enumerate(videos):
        print(num, video['snippet']['title'])


indianpythonistaChannelId = 'UCkUq-s6z57uJFUFBvZIVTyg'
socraticaChannelId= 'UCW6TXMZ5Pq6yL6_k5NZ2e0Q'
burooj_instituteChannelId = 'UCurWauB5suHGJXBuxd1IUTA'


videos = get_channel_videos(burooj_instituteChannelId)



