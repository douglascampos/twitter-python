#!/usr/local/bin/python2.7

import twitter
import json

# Import local classses
import util
import trending
import auth
import search



# Authentication in twitter-api
twitter_api = auth.login();

print "TWITTER API => ", twitter_api


print " 1 - Trending topics Brazil"
print " 2 - Trending topics World"
print " 3 - Trending topics Brazil - JSON "
print " 4 - Trending topics World  - JSON"
print " 5 - Common trends Brazil World "
print " 6 - Search on twitter "
print " 7 - Exit"

know_options = {
	"1":"Trending Topics Brazil",
	"2":"Trending Topics World",
	"3":"Trending Topics Brazil - JSON ",
	"4":"Trending Topics World  - JSON ",
	"5":"Common trends Brazil World",
	"6":"Search on Twitter",
	"7":"exit"
}

# util.clears();

opt = raw_input("Select option: ")
print "	=> "+ opt

print "option selected is: ", know_options[opt]

if opt == "1":
	trends_brz = trending.brazil(twitter_api);
	print "TRENDS BRAZIL"
	print
	print trends_brz
elif opt == "2":
	trends_world = trending.world(twitter_api);
	print "TRENDS WORLD"
	print
	print trends_world
elif opt == "3":
	brz_json = trending.brazil_json(twitter_api);
	print "JSON"
	print
	print "brz_json"

