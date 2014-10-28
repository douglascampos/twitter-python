#/usr/local/bin/python2.7

import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = '17Z8N69VA159zlqqvHJ8eYfxe'
CONSUMER_SECRET ='5eY3JwFZJvWK2wECgikax5o0LNcsbIdF4AnW0l88OVCA6gzXK8'
OAUTH_TOKEN = '17965973-qOvVvjtNebzmRx7KSTUGssjLLrI0Rew3RTaTFCmh1'
OAUTH_TOKEN_SECRET = 'E0LvKUlxJnK4vTRppTTgn9eElbMLgny5tUMwXOtk8BiTc'


def login():
	
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

	twitter_api = twitter.Twitter(auth=auth)

	# Nothing to see by displaying twitter_api except that it's now a
	# defined variable

	return twitter_api


