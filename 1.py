'''
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class" :"pagination"})

links = pagination.find_all("a")
pages = []
for link in links[:-1] :
  pages.append(int(link.string))#pages.append(int(link.find("span").string))

max_page = print(pages[-1]) # 마지막 페이지
'''
