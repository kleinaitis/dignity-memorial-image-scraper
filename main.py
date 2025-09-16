import json
import urllib.request
import requests
from bs4 import BeautifulSoup


def download_images(image_url_list):
    session = requests.Session()
    for i, image_url in enumerate(image_url_list):
        file_name = f"photo{i}.jpg"
        response = session.get(image_url)
        with open(file_name, 'wb') as file:
            file.write(response.content)


def fetch_memory_list(obituary_url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    request = urllib.request.Request(obituary_url, headers=headers)

    r = urllib.request.urlopen(request).read()
    html = r.decode('utf-8')

    soup = BeautifulSoup(html, "html.parser")

    script_tag = soup.find("script", id="__NEXT_DATA__")

    parse = json.loads(script_tag.contents[0])

    return parse["props"]["pageProps"]["memoryData"]["MemoryList"]


def build_image_urls(site_entries):

    url_list = []

    for entry in site_entries:
        image_parts = entry["Image"]
        if image_parts is not None:
            # Get parts of the URL in reverse order (index 13 -> 0)
            parts = [image_parts["FullUrl"][i] for i in range(13, -1, -1)]

            # Join parts with '/' to reconstruct the full URL
            url = "/".join(parts)

            url_list.append(url)

    return url_list


memory_list = fetch_memory_list("https://www.dignitymemorial.com/obituaries/dallas-tx/richard-cole-7245321")
url_list = build_image_urls(memory_list)
download_images(url_list)
