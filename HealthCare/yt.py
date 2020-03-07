import re

from bs4 import BeautifulSoup
from requests import get


def clean(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = s.replace("\n", "")
    s = s.replace("\t", "")
    s = s.lower()
    return s


def yt_scrape():
    r = get('https://www.youtube.com/playlist?list=PLui6Eyny-Uzwzd-9fi_cmhz3UW9gS1raf')
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')
    res = soup.find_all('a', {'class': 'pl-video-title-link'})
    for l in res:
        print("https://www.youtube.com" + l.get("href"))
