'''小說狂人爬蟲 貼上該書網址即可'''

import requests
from bs4 import BeautifulSoup
from novel import extract_inner_text
import os

def crawl(url):
    chapter_urls = []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find('span', class_ = 'title').get_text()

            for link in soup.find_all('a', href=True):
                href = link.get('href')
                # Ensure href is a full URL or make it one
                if href.startswith('http'):
                    full_url = href
                else:
                    full_url = "https:" + href

                # Check if the URL contains the desired substring
                if url in full_url:
                    chapter_urls.append(full_url)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    return title, chapter_urls

if __name__ == "__main__":

    start_url = [ 
                "https://czbooks.net/n/cgjfho"
                ]

    for i in start_url:
        title, chapters = crawl(i)

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = script_dir + '/' + title + '.txt'
        print(filename)
        with open(filename, 'a', encoding="utf_8_sig") as f:
            f.write(title)
            f.write("\n")

        for url in chapters:
            print(url)
            extract_inner_text(filename, url)