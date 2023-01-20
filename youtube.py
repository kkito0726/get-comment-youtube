import requests
import pandas as pd

with open("./API_KEY.txt", "r") as f:
    API_KEY = f.read()
    
class Youtube:
  def __init__(self, channel_id, max_results=50) -> None:
    self.channel_id = channel_id
    params = {
      "key": API_KEY,
      "part": "snippet",
      "channelId": channel_id,
      "maxResults": 50
    }
    res = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
    data = res.json()
    self.name = data['items'][0]['snippet']['channelTitle']
    self.videos = data
  
  def get_comments(self, video_id, max_results=100):
    params = {
      'key': API_KEY,
      'part': 'snippet',
      'videoId': video_id,
      'order': 'relevance',
      'textFormat': 'plaintext',
      'maxResults': max_results,
    }
    
    res = requests.get("https://www.googleapis.com/youtube/v3/commentThreads", params=params)
    comments = res.json()
    
    return comments

if __name__ == '__main__':
  syu = Youtube("UC1l8jsqYmIj1bjCzN43UPfA")
  print(syu.videos)