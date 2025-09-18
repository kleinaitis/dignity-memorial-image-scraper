import argparse
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
from pathlib import Path


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

            # "Condolences" image URLs are returned without a scheme (no http:// or https://)
            # Add https:/ since joining parts produces one extra / at the end
            if not url.startswith("http"):
                url = "https:/" + url

            url_list.append(url)

    return url_list


def download_images(image_url_list):
    session = requests.Session()
    downloads_folder = Path.home() / "Downloads"
    target_folder = downloads_folder / "ObituaryPhotos"
    target_folder.mkdir(parents=True, exist_ok=True)

    for i, image_url in enumerate(image_url_list):
        file_name = f"photo{i}.jpg"
        file_path = target_folder / file_name

        response = session.get(image_url)
        with open(file_path, 'wb') as file:
            file.write(response.content)


def main(obituary_url):
    memory_list = fetch_memory_list(obituary_url)
    url_list = build_image_urls(memory_list)
    download_images(url_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download all images from a Dignity Memorial obituary page.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog = "Example:\n  python main.py https://www.dignitymemorial.com/obituaries/john-doe-12345",
    )
    parser.add_argument(
        "url",
        help="The full URL of the obituary page (e.g., https://www.dignitymemorial.com/obituaries/...)."
    )
    args = parser.parse_args()

    main(args.url)

