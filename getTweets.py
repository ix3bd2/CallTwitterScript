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



latestSocialUrl = "https://api.genshinworldrecords.com/latest_socials/3"

latestSocialPayload = json.dumps({
  "tweets": [
    tweet1
  ]
})
latestSocialHeaders = {
  'Content-Type': 'application/json'
}

response1 = requests.request("PUT", latestSocialUrl, headers=latestSocialHeaders, data=latestSocialPayload)

print(response1.text)
print(tweet2)