const inputApiRef = document.querySelector("#api-key");
const inputVideoIdRef = document.querySelector("#video-id");
const inputChannelIdRef = document.querySelector("#channel-id");
const channelSubmitButtonRef = document.querySelector("#channelSubmit");
const submitButtonRef = document.querySelector("#submit");

const getVideoTitle = async (API_KEY, channelId) => {
  const URL = "https://www.googleapis.com/youtube/v3/search";

  const params = {
    key: API_KEY,
    part: "snippet",
    channelId: channelId,
    maxResults: 50,
  };
  const query_params = new URLSearchParams(params);

  const res = await fetch(`${URL}?${query_params}`);
  const data = await res.json();
  console.log(data);
};

const getComments = async (API_KEY, videoId, maxResults) => {
  const URL = "https://www.googleapis.com/youtube/v3/commentThreads";
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

  console.log(data);
};

channelSubmitButtonRef.addEventListener("click", () => {
  const API_KEY = inputApiRef.value;
  const channelId = inputChannelIdRef.value;
  if (API_KEY && channelId) {
    getVideoTitle(API_KEY, channelId, 50);
  } else {
    alert("入力内容が不十分です");
  }
});

submitButtonRef.addEventListener("click", () => {
  const API_KEY = inputApiRef.value;
  const videoId = inputVideoIdRef.value;
  if (API_KEY && videoId) {
    getComments(API_KEY, videoId, 100);
  } else {
    alert("入力内容が不十分です");
  }
});
