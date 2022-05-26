import requests
import json

url = "https://api.twitter.com/2/users/1072404907230060544/tweets"

payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAAGVTwEAAAAALnihM2GNXt9EkV%2B8EJFEuqloZNY%3DtBTwdZrSJf15YxU5kuwbfPAPjMFdLp551nzT3a0xlkELWvDIE5',
  'Cookie': 'guest_id=v1%3A165289794183344721'
}

response = requests.request("GET", url, headers=headers, data=payload)
parse_json = json.loads(response.text)
tweet1 = parse_json['data'][0]['id']
tweet2 = parse_json['data'][1]['id']

urlemb = "https://publish.twitter.com/oembed?url=https://twitter.com/GenshinImpact/status/" + tweet1

payloademb={}
headersemb = {
  'Cookie': 'guest_id=v1%3A165289794183344721; guest_id_ads=v1%3A165289794183344721; guest_id_marketing=v1%3A165289794183344721; personalization_id="v1_R87GhHRNyEFy7aXKDzGvEw=="'
}

responseemb = requests.request("GET", urlemb, headers=headersemb, data=payloademb)
parse_jsonemb = json.loads(responseemb.text)
tweetenb = parse_jsonemb['html']

urlYT = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCiS882YPwZt1NfaM0gR0D9Q&maxResults=10&order=date&type=video&key=AIzaSyDlVaWM4TB8jhSohVEKidDw6Ba9nt_iZ2Q"

payloadYT={}
headersTY = {}

responseTY = requests.request("GET", urlYT, headers=headersTY, data=payloadYT)
parse_jsonYT = json.loads(responseTY.text)
dataYt = parse_jsonYT['items'][0]['id']['videoId']
print(dataYt)

latestSocialUrl = "https://api.genshinworldrecords.com/latest_socials/3"

latestSocialPayload = json.dumps({
  "tweets": [
    tweetenb
  ],
  "youtubeVideo": dataYt
})
latestSocialHeaders = {
  'Content-Type': 'application/json'
}

response1 = requests.request("PUT", latestSocialUrl, headers=latestSocialHeaders, data=latestSocialPayload)

print(response1.text)
print(tweet2)