#!/usr/bin/env python

import requests
import lxml.html
from StringIO import StringIO

baseurl = "http://www.oshoworld.com/discourses/"
input_urls = ["http://www.oshoworld.com/discourses/audio_hindi.asp?cat=All",
              "http://www.oshoworld.com/discourses/audio_eng.asp?cat=All"]
output_urls = set()

for url in input_urls:
    r = requests.get(url)
    content = StringIO(r.text)

    document = lxml.html.parse(content).getroot()
    document.make_links_absolute(baseurl)

    for(_, _, link, _) in document.iterlinks():
        output_urls.add(link)

output_urls = [output_url for output_url in output_urls if "album_id=" in output_url]

with open("stage2.txt", "w") as f:
    f.write("\n".join(output_urls))
