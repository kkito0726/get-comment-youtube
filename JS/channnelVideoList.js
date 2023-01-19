const fetch = require("node-fetch");
const fs = require("fs");

const URL = "https://www.googleapis.com/youtube/v3/search";
const API_KEY = fs.readFileSync("./API_KEY.txt", "utf8");

const getVideoTitle = async (channelId) => {
  const params = {
    key: API_KEY,
    part: "snippet",
    channelId: channelId,
    maxResults: 50,
  };
  const query_params = new URLSearchParams(params);

  const res = await fetch(`${URL}?${query_params}`);
  const data = await res.json();
  const items = data.items;
  const channelName = items[0].snippet.channelTitle;
  const titles = [];
  const videoIds = [];
  items.map((item) => {
    titles.push(item.snippet.title);
    videoIds.push(item.id.videoId);
  });
  console.log(channelName);
  console.log(titles);
  console.log(videoIds);
};

const channelId = "UC1l8jsqYmIj1bjCzN43UPfA";
getVideoTitle(channelId);
