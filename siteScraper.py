import requests
from bs4 import BeautifulSoup
from pprint import pprint

def getootbalitarinatestews():
    urls = requests.get('http://footballitarin.com/links.php')
    urls.raise_for_status()
    baseurl ='http://footballitarin.com/link_page.php'
    fname = 'footbalitarin_latest_news'

    data = urls.text
    #print(data)
    soup = BeautifulSoup(data, features='lxml')
    latestNews = soup.find_all('div', {'class': 'news_title'})
    # print(f'the length is {len(latestNews)}')
    with open('/Users/XZY/Desktop/'+fname+'.html', 'w') as f:
        for l in latestNews:
            for news in latestNews:
                # print(news)
                for n in news:
                    # print(n)
                     #str(n).replace('link_page.php', baseurl)
                     f.write('<li>' + str(n).replace('link_page.php', baseurl) + '</li>')
    print('Successfully received the latest news from Footbalitarin Website!\n\n')

    with open('/Users/XZY/Desktop/'+fname+'.html', 'r') as f:
         for _ in f:
            pprint(_)

getootbalitarinatestews()
