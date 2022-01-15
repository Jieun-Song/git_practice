import re
from website_download import download

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    html = download(links)

crawl_sitemap("https://linkareer.com/list/activity?filterBy_interestIDs=13&filterType=INTEREST&orderBy_direction=DESC&orderBy_field=CREATED_AT&page=1")