import requests
import pandas as pd

URL = 'https://www.googleapis.com/youtube/v3/'

def get_comments(no, video_id, next_page_token, max_results=100):
  params = {
    'key': API_KEY,
    'part': 'snippet',
    'videoId': video_id,
    'order': 'relevance',
    'textFormat': 'plaintext',
    'maxResults': max_results,
  }
  if next_page_token is not None:
    params['pageToken'] = next_page_token
  res = requests.get(f'{URL}commentThreads', params=params)
  data = res.json()
  
  return data

def json2dataframe(data):
  items = data['items']
  comment_list = [items[i]['snippet']['topLevelComment']['snippet'] for i in range(len(items))]
  
  authors = [item['authorDisplayName'] for item in comment_list]
  published_at = [item['publishedAt'] for item in comment_list]
  updated_at = [item['updatedAt'] for item in comment_list]
  comments = [item['textDisplay'] for item in comment_list]
  like_count = [item['likeCount'] for item in comment_list]
  author_channel_url = [item['authorChannelUrl'] for item in comment_list]
  
  df = pd.DataFrame()
  df['authorDisplayName'] = authors
  df['Published_at'] = published_at
  df['publishedAt'] = updated_at
  df['textDisplay'] = comments
  df['likeCount'] = like_count
  df['authorChannelUrl'] = author_channel_url
  
  return df
  

if __name__ == '__main__':
  with open("./API_KEY.txt", "r") as f:
    API_KEY = f.read()
  
  video_id = "IWRwInTMo9c"
  no = 1
  data = get_comments(no, video_id, None)
  df = json2dataframe(data)
  
  df.to_csv("./csv/output.csv", encoding="shift-jis")
  print(df)