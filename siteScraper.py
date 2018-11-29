import requests
from bs4 import BeautifulSoup
from pprint import pprint


def getootbalitarinatestews():

    proxies ={
        'http_proxy' : 'http://proxy2.isis.airnz.co.nz:5865',
        'https_proxy': 'https://proxy2.isis.airnz.co.nz:5865'
    }

    urls = requests.get('http://footballitarin.com/links.php')
    urls.raise_for_status()
    baseurl ='http://footballitarin.com/link_page.php'
    fname = 'footbalitarin_latest_news'

    data = urls.text
    #print(data)
    soup = BeautifulSoup(data, features='lxml')
    latestNews = soup.find_all('div', {'class': 'news_title'})
    # print(f'the length is {len(latestNews)}')
    with open('/Users/asgarh/Desktop/'+fname+'.html', 'w') as f:
        for _ in latestNews:
            for news in latestNews:
                # print(news)
                for n in news:
                    # print(n)
                     #str(n).replace('link_page.php', baseurl)
                     f.write('<li>' + str(n).replace('link_page.php', baseurl) + '</li>')
    print('Successfully received the latest news from Footbalitarin Website!\n\n')

    with open('/Users/asgarh/Desktop/'+fname+'.html', 'r') as f:
            for _ in f:
                pprint(_)


getootbalitarinatestews()
