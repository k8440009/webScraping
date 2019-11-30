import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# indeed 페이지 추출


def extract_indeed_pages():
    indeed_result = requests.get(URL)

    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    pagination = indeed_soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        # pages.append(int(link.find("span").string))
        pages.append(int(link.string))

    max_page = pages[-1]  # 마지막 페이지
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all(
        "div", {"class": "jobsearch-SerpJobCard"})  # 일자리 추출
    for result in results:
        title = result.find("div", {"class": "title"}).find("a")[
            "title"]   # 제목 추출
        print(title)
    return jobs
