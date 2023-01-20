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
    
  def output_videos(self):
    items = self.videos['items']
    titles = [item['snippet']['title'] for item in items]
    published_time = [item['snippet']['publishTime'] for item in items]
    videoIds = [item['id']['videoId'] for item in items]
    thumbnails = [item['snippet']['thumbnails']['high']['url'] for item in items]
    
    df = pd.DataFrame()
    df['title'] = titles
    df['publishedTime'] = published_time
    df['videoId'] = videoIds
    df['thumbnail'] = thumbnails
    
    df.to_csv(f"./csv/{self.name}_video_info.csv", encoding="shift-jis")
    return df
  
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
  channel_id = input("Channel IDを入力: ")
  ch = Youtube(channel_id)
  df_videos = ch.output_videos()
  print(df_videos)