# Obituary Photo Downloader

After my dad passed away, I wanted to save all the photos from his Dignity Memorial obituary page, but there wasn’t an easy way to download hundreds of images at once. I built this tool to help me do that. I hope it can help you preserve memories too.

This tool allows you to download all images from a Dignity Memorial obituary page into a folder on your computer. It’s designed to be simple for anyone to use, whether you’re comfortable with Python or just want a one-click solution.

---

## How It Works

1. You provide the URL of a Dignity Memorial obituary page
2. The tool fetches all the images linked on that page
3. It saves them to a folder called `ObituaryPhotos` inside your `Downloads` directory 

This makes it easy to quickly gather all the photos in one place without manually saving each image.

---

## Getting Started

### Example URL

The tool expects a full obituary page URL. For example:

> https://www.dignitymemorial.com/obituaries/john-doe-12345


Make sure you copy the **entire URL** from your browser.

---

## Quick Start (No Python Required)

A standalone .exe is available for Windows, so you don’t need Python:

1. Download `ObituaryPhotoDownloader.exe` from the [Releases page](https://github.com/kleinaitis/dignity-memorial-image-scraper/releases/)
2. Double-click the .exe to open a terminal window
3. Paste the obituary URL when prompted
4. Photos will be saved to `ObituaryPhotos` in your `Downloads` folder
5. A message will confirm when the download is complete

This approach is meant to be simple and friendly — you don’t need to type anything in the command line beyond pasting the URL.

> If you prefer to run the script directly rather than using the `.exe`, see the [Developer Instructions](#developer-instructions-optional) section.

## Notes

* This tool is specifically designed for Dignity Memorial obituary pages. Other websites will **not** work
* Developers can still use the Python script if they want more control
* The .exe is intended for non-technical users - just paste the URL and download the photos

### Developer Instructions (Optional)

<details>
<summary>For Developers</summary>

If you’re familiar with Python, you can run the script directly from the terminal by doing the following.

Clone the project:

```
git clone https://github.com/kleinaitis/dignity-memorial-image-scraper.git
cd dignity-memorial-image-scraper
```

Then install the required dependencies:

```
pip install -r requirements.txt
```

After installing the dependencies, run the script with your obituary URL by replacing `<URL>` in the command below:


```
python main.py <URL>
``` 

</details>