#pip install TwitterAPI
from TwitterAPI import TwitterAPI
import sys
import json

#consumer
consumer_key = 'NZgTx9Oqe2ePnlwtPktgKLoCD'
consumer_secret = 'ZwrqJ5mgB5evpPm1jNNfpWPJ2DSlttFeIx3Ax2z0Rlk15uvc8g'

#token
access_token = 	'77996537-YzG4ydANL8xsmbKClpEb4pvV3BwMYgt0VZYREFy6Y'
access_token_secret = 'KlxURzE21r7HFPTjmiHpoXecIX7b0WfnyCyjekFnSRn34'


api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

r = api.request('search/tweets', {'q':'refugees','since':'2016-05-08','lang':'en'})

itemList = []
entitiesList = []
for item in r:
        print(item['text'].encode(sys.stdout.encoding, errors='replace'))
        print("\n")
        print(item['entities'])
        print("\n")
        entitiesList.append(item['entities'])
        itemList.append(item['text'].encode(sys.stdout.encoding, errors='replace'))


# with open('data.txt', 'w') as outfile:
#     json.dump(itemList, outfile)

with open('tweets.txt', 'w') as outfile:
	for item in itemList:
  		outfile.write("%s\n" % item)

with open('entities.txt', 'w') as outfile:
	for item in entitiesList:
  		outfile.write("%s\n" % item)