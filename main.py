from TwitterSearch import *
import json
import requests

destination_path = 'results/'

consumer_key = 	'gyd5Toe9MKxYvbtmduz7epUZp'
consumer_key_secret = '6CC67WHxe7lKOLvlRmJlmQvNzUII5Gt0CnQUeJu5cc0yqiWfrP'
access_token = '247776968-XTmwgKO7b3afttCdN4vu8NfeC8Xaf1kaozeCrLHO'
access_token_secret = 'UrnHLqYJ1GFNIff9kaVkJesz0AzRNLwhYqTGUt6Q9SF4U'
try:
    tso = TwitterUserOrder('KFC_UKI')
    # tso.set_keywords(['KFC', 'video'])
    # tso.set_source_filter('KFC_UKI')
    # tso.set_language('en')
    tso.set_include_entities(True)

    ts = TwitterSearch(
        consumer_key=consumer_key,
        consumer_secret=consumer_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    results = ts.search_tweets_iterable(tso)

except TwitterSearchException as e:
    print(e)

images = []
for i, tweet in enumerate(results):
#     if i > 10:
#         break
    with open('{1}{0}.json'.format(tweet['id_str'],destination_path), 'w') as jsonfile:
        json.dump(tweet, jsonfile, indent=4)
        jsonfile.close()
    # print(json.dumps(tweet, indent=4))
    if "media" in tweet["entities"]:
        for i, image in enumerate(tweet["entities"]["media"]):
            r = requests.get(image["media_url"])
            with open('{1}{0}_{2}.jpeg'.format(tweet['id_str'], destination_path, i), 'wb') as imagefile:
                for chunk in r:
                    imagefile.write(chunk)
                imagefile.close()
