import requests
import json

urlYT = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCiS882YPwZt1NfaM0gR0D9Q&maxResults=10&order=date&type=video&key=AIzaSyDlVaWM4TB8jhSohVEKidDw6Ba9nt_iZ2Q"

payloadYT={}
headersTY = {}

responseTY = requests.request("GET", urlYT, headers=headersTY, data=payloadYT)
print(responseTY.text)
parse_jsonYT = json.loads(responseTY.text)
dataYt = parse_jsonYT['items'][0]['id']['videoId']
print(dataYt)

latestSocialUrl = "https://api.genshinworldrecords.com/latest_socials/3"

latestSocialPayload = json.dumps({
  "youtubeVideo": dataYt
})
latestSocialHeaders = {
  'Content-Type': 'application/json'
}

response1 = requests.request("PUT", latestSocialUrl, headers=latestSocialHeaders, data=latestSocialPayload)