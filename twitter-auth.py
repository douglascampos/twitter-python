#!/usr/local/bin/python2.7

import twitter
import json

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = '17Z8N69VA159zlqqvHJ8eYfxe'
CONSUMER_SECRET ='5eY3JwFZJvWK2wECgikax5o0LNcsbIdF4AnW0l88OVCA6gzXK8'
OAUTH_TOKEN = '17965973-qOvVvjtNebzmRx7KSTUGssjLLrI0Rew3RTaTFCmh1'
OAUTH_TOKEN_SECRET = 'E0LvKUlxJnK4vTRppTTgn9eElbMLgny5tUMwXOtk8BiTc'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print twitter_api

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424768

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

#world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
#us_trends = twitter_api.trends.place(_id=US_WOE_ID)

#print world_trends
#print
#print us_trends

#print json.dumps(world_trends, indent=1)
#print
#print json.dumps(us_trends, indent=1)


#world_trends_set = set([trend['name'] 
#				                        for trend in world_trends[0]['trends']])

#us_trends_set = set([trend['name'] 
#				                     for trend in us_trends[0]['trends']]) 

#common_trends = world_trends_set.intersection(us_trends_set)

#print common_trends

# XXX: Set this variable to a trending topic, 
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.

q = '#Motorcycle' 

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print "Length of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break
        
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
print json.dumps(statuses[0], indent=1)

status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]

# Explore the first 5 items for each...

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1) 
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)

from collections import Counter
from prettytable import PrettyTable

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print pt

# ===========================================
#search_results = twitter_api.search.tweets(q="motorcycle", count=1)
#print search_results

# mytokenblablablatestepython
# mytokenblablablatestepythonsecret

#  curl --get 'https://api.twitter.com/1.1/' --data 'motorcycle=' --header 'Authorization: OAuth oauth_consumer_key="GzZvKRXnUnXLWvTrD5DQeUm53", oauth_nonce="eedc85e287fc88fe893fde9748e999c4", oauth_signature="0caOnJN2BorSUMCveHFa1DjuLAo%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1414443310", oauth_token="mytokenblablablatestepython", oauth_version="1.0"' --verbose
