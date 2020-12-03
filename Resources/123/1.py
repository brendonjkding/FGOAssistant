#!pypy3
import requests
from bs4 import BeautifulSoup
import re
from time import *
import random
import pickle
import urllib

proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080"
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    "user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    "user-agent": 'Opera/9.25 (Windows NT 5.1; U; en)',
    "user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    "user-agent": 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    "user-agent": 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    "user-agent": 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "}


def spider(url,name):
    flag = 1
    while flag:
        r = None
        try:
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                print("---------retrying")
                sleep(15)
                continue
            flag = 0

        except Exception:
            print("---------" + r.status_code)
            sleep(15)

    r.encoding = 'utf-8'
    html = r.text

    

    soup = BeautifulSoup(html, 'html.parser')

    file_out=open('1/'+name,'w')
    print(soup.prettify(),file=file_out)

    file_out.close()


if __name__ == "__main__":
    file_in=open("1.txt","r")
    txt=file_in.readline();
    lines=txt.split('\\n')
    # print(lines[0])

    for line in lines[268:]:
        # print(line)
        p=re.compile(r'([^,]*?,){5}([^,]*?),.*')
        r=p.match(line)
        name=r.group(2)
        print(name)
        url='https://'+urllib.parse.quote('fgo.wiki/w/'+name)
        print(url)

        spider(url,name)

        # break
        sleep(random.randint(10,15))

