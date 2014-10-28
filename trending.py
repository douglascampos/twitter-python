#/usr/local/bin/python2.7

import json

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/


def world(twitter_api):
	WORLD_WOE_ID = 1
	world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

	# world_trends_parse = parse_trending(world_trends);

	# print world_trends
	return world_trends


def brazil(twitter_api):
	BR_WOE_ID = 23424768 # Brasil

	br_trends = twitter_api.trends.place(_id=BR_WOE_ID)

	#	br_trends_parse = parse_trending(br_trends);

	# print br_trends
	return br_trends


def parse_trending(trending):
	trends_set = set([trend['name']
		for trend in trending[0]['trends']])
	return trends_set


def world_json(twitter_api):
	wld = world(twitter_api);
	# print json.dumps(world, indent=1)
	return json.dumps(wld, indent=1)


def brazil_json(twitter_api):
	brz = brazil(twitter_api);
	# print json.dumps(brz, indent=1)
	return json.dumps(brz, indent=1)
	

def common_trends(twitter_api):
	world_trends_set = set([trend['name'] 
		for trend in world_trends[0]['trends']])

	br_trends_set = set([trend['name'] 
		for trend in br_trends[0]['trends']]) 

	common_trends = world_trends_set.intersection(br_trends_set)

	# print common_trends
	return common_trends


