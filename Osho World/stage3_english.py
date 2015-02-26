#!/usr/bin/env python

english_baseurl = "http://www.oshoarchive.com/ow-english/"

with open("english.txt", "r") as f:
    for line in f:
        track = line.strip()
        print english_baseurl + track
