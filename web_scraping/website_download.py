from urllib import request
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re

def download(url, user_agent='wswp',num_retries = 2):
    print("downloading:", url)
    headers = {'User-agent':user_agent}
    request = Request(url, headers=headers)
    try:
        html = urlopen(url).read().decode("utf-8")
    except HTTPError as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                #5xx Http 오류 시 재시도
                return download(url, num_retries -1)
    return html
    #URL이 전달됐을때 웹 페이지를 다운로드 하고 HTML을 반환한다.

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    html = download(links)

crawl_sitemap("https://linkareer.com/list/activity?filterBy_interestIDs=13&filterType=INTEREST&orderBy_direction=DESC&orderBy_field=CREATED_AT&page=1")