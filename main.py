import webbrowser as b
from bs4 import BeautifulSoup
import requests as req
import re

base_url = 'https://www.google.com/search?{}&tbm=isch&tbs={}'

def build_new_url(resp):
    # do request, find first tbs=rimg: thingy?
    # reconstruct as base_url.format(currentQuery, new rimg)
    pass

matcher = re.compile(r'tbs=(.*)tbo', re.UNICODE)

def get_rimg(imgurl, imgrefurl, imgdii):
    base_url = "https://images.google.com/async/imgrc?sync=q:,cidx:1,_id:irc_imgrc1,_pms:il&imgurl={}&imgdii={}"
    # TODO properly escape all inputs?
    # Fake a user-agent.
    res = req.get(url=base_url.format(imgurl, imgdii),
                  headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    html = res.text
    capture = matcher.search(html)
    output = capture.group()[4:-13] if capture is not None else None
    print(output)
    return output
query = "q=yolo"
related_image = "rimg:CRf44LCsIKPWIjgHPKrSKSA9RgkrU0rv6SNS40Mr-Xye6oMiNhvZ8bJApImAzELNAdhHDOIOpk7hnzjYICNSdIxNJCoSCQc8qtIpID1GEaDcXcaJLneYKhIJCStTSu_1pI1IRNjFzQf6az-MqEgnjQyv5fJ7qgxFMUz83obL3AioSCSI2G9nxskCkEZkYsd5LhrSJKhIJiYDMQs0B2EcRUtl0L4pxGCkqEgkM4g6mTuGfOBEZ_1hzri_1ch6CoSCdggI1J0jE0kEYb-U9cxX9gM"
prev_url = ""

# TODO no query-param
# TODO add incognito mode.

# TODO continue here
#html = req.get(base_url.format(query, related_image), {'Accept-Encoding': 'identity'}).text
#res = req.get("https://www.google.no/imgres?&imgrefurl=https%3A%2F%2Fpjreddie.com%2Fdarknet%2Fyolo%2F&docid=9EGD1Tr6B7ZL2M&tbnid=n4bqt5eyX0i8yM%3A")
# TODO get imgurl, imgdii
imgurl = "https%3A%2F%2Fpjreddie.com%2Fmedia%2Fimage%2Fyologo_1.png"
#imgrefurl = "https%3A%2F%2Fpjreddie.com%2Fdarknet%2Fyolo%2F"
imgdii = "n4bqt5eyX0i8yM%3A"
get_rimg(imgurl, imgdii)
#loop = asyncio.get_event_loop()
#loop.run_until_complete(test(loop))

# if prev_url, use prev_url and strip out query somehow?
#prev_url = base_url.format("{}", related_image)

#print(base_url.format("", related_image))

#b.get(["Chrome", "%s", "--incognito"]).open(prev_url if prev_url != "" else base_url.format(query, related_image))
#print(b.get().args)

#b.open(prev_url if prev_url != "" else base_url.format(query, related_image))
#b.open(prev_url if prev_url != "" else base_url.format("", related_image))