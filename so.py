import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    print(pages)


'''
def get_jobs():
    last_page = get_last_page()
        return []
'''
