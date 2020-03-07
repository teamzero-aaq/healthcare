import re

from bs4 import BeautifulSoup
from requests import get


def clean(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = s.replace("\n", "")
    s = s.replace("\t", "")
    s = s.lower()
    return s


def news_scrape():
    url = "https://techcrunch.com/health/"
    response = get(url)
    print(response)
    page_soup = BeautifulSoup(response.content, 'html.parser')
    raw_data = page_soup.findAll('a', {'class': 'post-block__title__link'})

    data = []
    if raw_data:
        for rd in raw_data:
            datnum = {}
            datnum['links'] = rd.get('href')
            datnum['text'] = clean(rd.text)
            data.append(datnum)
        print(data)
