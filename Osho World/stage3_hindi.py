#!/usr/bin/env python

hindi_baseurl = "http://www.oshoarchive.com/ow-hindi/"

with open("hindi.txt", "r") as f:
    for line in f:
        track = line.strip()
        print hindi_baseurl + track
