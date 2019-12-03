import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# indeed 페이지 추출


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        # pages.append(int(link.find("span").string))
        pages.append(int(link.string))
    max_page = pages[-1]  # 마지막 페이지
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]   # 제목 추출
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        # 회사 링크가 없는 경우
        if company_anchor is not None:
            company = str(company_anchor.string)
        # 링크가 있는 경우
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title,
            'company': company,
            'location': location,
            'link': f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Indeed scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all(
            "div", {"class": "jobsearch-SerpJobCard"})  # 일자리 추출
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_pages = get_last_pages()
    jobs = extract_jobs(last_pages)
    return jobs
