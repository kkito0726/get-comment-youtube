const fetch = require("node-fetch");
const fs = require("fs");

const URL = "https://www.googleapis.com/youtube/v3/commentThreads";
const API_KEY = fs.readFileSync("./API_KEY.txt", "utf8");

const get_comment = async (videoId, maxResults) => {
  const params = {
    key: API_KEY,
    part: "snippet",
    videoId: videoId,
    order: "relevance",
    textFormat: "plainText",
    maxResults: maxResults,
  };
  const query_params = new URLSearchParams(params);

  const res = await fetch(`${URL}?${query_params}`);
  const data = await res.json();
  items = data.items;
  comments = [];
  items.map((item) => {
    comments.push(item.snippet.topLevelComment.snippet.textDisplay);
  });
  console.log(comments);
};

const videoId = "IWRwInTMo9c";
get_comment(videoId, 100);
