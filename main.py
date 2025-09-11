import json
import re
import urllib.request
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
url = "https://www.dignitymemorial.com/obituaries/dallas-tx/richard-cole-7245321"
request = urllib.request.Request(url, headers=headers)

r = urllib.request.urlopen(request).read()
html = r.decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

script_tag = soup.find("script", id="__NEXT_DATA__")

parse = json.loads(script_tag.contents[0])
print(parse["props"]["pageProps"]["memoryData"]["MemoryList"][0])
