# -*- coding: utf-8 -*-
import webbrowser as b
from bs4 import BeautifulSoup
import requests as req
import re
import json
from _collections import OrderedDict
from urllib.parse import quote

# Fake a user-agent.
user_agent_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

base_url = 'https://www.google.com/search?{}&tbm=isch&tbs={}'

def build_new_url(resp):
    # do request, find first tbs=rimg: thingy?
    # reconstruct as base_url.format(currentQuery, new rimg)
    pass

matcher = re.compile(r'tbs=(.*)tbo', re.UNICODE)


def get_rimg(imgurl, imgdii):
    base_url = "https://images.google.com/async/imgrc?async=q:,cidx:1,_id:irc_imgrc1,_pms:il&imgurl={}&imgdii={}"
    res = req.get(url=base_url.format(quote(imgurl), quote(imgdii)),
                  headers=user_agent_header)
    html = res.text
    capture = matcher.search(html)
    output = capture.group()[4:-13] if capture is not None else None
    print(output)
    return output

def get_initial_images(ggl_img_url):
    resp = req.get(ggl_img_url, headers=user_agent_header)
    soup = BeautifulSoup(resp.text, 'lxml')
    img_divs = soup.findAll("div", {"class": "rg_meta"})
    div_dicts = OrderedDict()  # we return in order
    for div in img_divs:
        try:
            d = json.loads(div.text)
            div_dicts[d['id']] = d
        except:
            pass
    print(div_dicts)
    return div_dicts

query = "q=yolo"
#query = ""
#related_image = "rimg:CRf44LCsIKPWIjgHPKrSKSA9RgkrU0rv6SNS40Mr-Xye6oMiNhvZ8bJApImAzELNAdhHDOIOpk7hnzjYICNSdIxNJCoSCQc8qtIpID1GEaDcXcaJLneYKhIJCStTSu_1pI1IRNjFzQf6az-MqEgnjQyv5fJ7qgxFMUz83obL3AioSCSI2G9nxskCkEZkYsd5LhrSJKhIJiYDMQs0B2EcRUtl0L4pxGCkqEgkM4g6mTuGfOBEZ_1hzri_1ch6CoSCdggI1J0jE0kEYb-U9cxX9gM"
related_image = ""
prev_url = ""

# TODO no query-param
# TODO add incognito mode.

# TODO continue here
b.open(base_url.format(query, related_image))
img_dict = get_initial_images(base_url.format(query, related_image))

k, dv = list(img_dict.items())[16]
print(k, dv)
rimg_tag = get_rimg(dv['ou'], k)  # ou = original url
b.open(base_url.format(query, rimg_tag))

#resp = req.get(base_url.format(query, related_image), headers=user_agent_header)
#html = resp.content
#print(BeautifulSoup(html, 'lxml').prettify())
#print(resp.url)
# TODO get imgurl, imgdii
# TODO show comparison of first search-word and new?
imgurl = "https%3A%2F%2Fpjreddie.com%2Fmedia%2Fimage%2Fyologo_1.png"
#imgrefurl = "https%3A%2F%2Fpjreddie.com%2Fdarknet%2Fyolo%2F"
imgdii = "n4bqt5eyX0i8yM%3A"
#get_rimg(imgurl, imgdii)

# if prev_url, use prev_url and strip out query somehow?
#prev_url = base_url.format("{}", related_image)

#print(base_url.format("", related_image))

#b.get(["Chrome", "%s", "--incognito"]).open(prev_url if prev_url != "" else base_url.format(query, related_image))
#print(b.get().args)

#b.open(prev_url if prev_url != "" else base_url.format(query, related_image))
#b.open(prev_url if prev_url != "" else base_url.format("", related_image))