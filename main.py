#!/usr/local/bin/python2.7

import util
import trending
import auth
import search

print " 1 - Trending topics "
print " 2 - Search on twitter "

know_options = {
	"1":"Trending Topics",
	"2":"Search on Twitter",
	"3":"exit"
}

def trending():
	util.clears();
	print "SHOW TRENDING TOPICS";

	return;

opt = raw_input("Selection option: ")
print "	=> " + opt

print "option selected is: ", know_options[opt]

if opt == "1":
	trending();
elif opt == 2:
	search();

def search():
	print "Search on Twitter function";
	return;


