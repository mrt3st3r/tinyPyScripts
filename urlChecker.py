from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import sys

def linkChecker(baseURL):
    resp = requests.get(baseURL)
    soup = BeautifulSoup(resp.content, features="lxml")
    valid_urls = []
    for links in soup.find_all("a", href=True):
        if links["href"].startswith("http"):
            valid_urls.append(links["href"])
    unique_urls = []
    for url in valid_urls:
        if url not in unique_urls:
            unique_urls.append(url)
    for url in unique_urls:
        r = requests.get(url)
        if r.status_code in (200, 999):
            print("PASS  >>> " + url + "  >>>  " + str(r.status_code))
        else:
            print("FAILED   >>>     " + str(r.status_code))
            sys.exit(-1) # mark the test as failure if non 200
    print("All done!")
    print(f"Total number of urls tested: {len(valid_urls)}")


if __name__ == "__main__":
    linkChecker("https://www.contact.co.nz")
