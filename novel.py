import requests
from bs4 import BeautifulSoup

def extract_inner_text(filename, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # # Extracting the inner text of a specific div with a class name
            specific_div = soup.find('div', class_='content')

            try:
                with open(filename, 'a', encoding="utf_8_sig") as f:
                    f.write(specific_div.get_text(strip="<br/>", separator="\n"))
                    f.write("\n\n")
            except Exception as e:
                print(f"Failed: {e}")
        else:
            print(f"Failed to retrieve page: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# if __name__ == "__main__":
#     title = "123"
#     url = "https://czbooks.net/n/cpg6i8n/blio6?chapterNumber=25"
#     extract_inner_text(title, url)
