import requests

URL = 'https://www.googleapis.com/youtube/v3/'

def get_comments(no, video_id, next_page_token):
  params = {
    'key': API_KEY,
    'part': 'snippet',
    'videoId': video_id,
    'order': 'relevance',
    'textFormat': 'plaintext',
    'maxResults': 100,
  }
  if next_page_token is not None:
    params['pageToken'] = next_page_token
  res = requests.get(f'{URL}commentThreads', params=params)
  data = res.json()
  
  return data

if __name__ == '__main__':
  API_KEY = input("API KEYを入力: ")
  
  video_id = "IWRwInTMo9c"
  no = 1
  data = get_comments(no, video_id, None)
  print(data)