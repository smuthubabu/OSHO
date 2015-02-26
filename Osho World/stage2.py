#!/usr/bin/env python

import requests
from pyquery import PyQuery as pq

hindi_tracks = open("hindi.txt", "w")
# english_tracks = open("english.txt", "w")


def process_url(url):
    print url
    is_english = "audio_eng" in url
    if is_english:
        print "Skipping ..."
        return
    r = requests.get(url)

    # extract "trackvalue" values from this page
    d = pq(r.text)
    for item in d.find('input[name="trackvalue"]'):
        track = item.value
        output = "%s\n" % track
        if is_english:
            # english_tracks.write(output)
            pass
        else:
            hindi_tracks.write(output)

    hindi_tracks.flush()
    # english_tracks.flush()


with open("stage2.txt", "r") as f:
    for line in f:
        url = line.strip()
        process_url(url)
