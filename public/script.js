const inputApiRef = document.querySelector("#api-key");
const inputVideoIdRef = document.querySelector("#video-id");
const submitButtonRef = document.querySelector("#submit");

const URL = "https://www.googleapis.com/youtube/v3/commentThreads";

const get_comment = async (API_KEY, videoId, maxResults) => {
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

submitButtonRef.addEventListener("click", () => {
  const API_KEY = inputApiRef.value;
  const videoId = inputVideoIdRef.value;
  if (API_KEY && videoId) {
    get_comment(API_KEY, videoId, 100);
  } else {
    alert("入力内容が不十分です");
  }
});
