import json
import os
import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.duitang.com',
    'Referer': 'https://www.duitang.com/search/?kw=iu&type=feed',
    'Accept': 'application/json, text/javascript',
}
url = 'https://mm.taobao.com/self/aiShow.htm?userId=865838484'
response = requests.get(url)
file = open("test.html","w")
file.write(response.text)
