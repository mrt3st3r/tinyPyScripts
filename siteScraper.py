import requests
from bs4 import BeautifulSoup
from pprint import pprint


def getootbalitarinatestews():

    proxies ={
        'http_proxy' : 'http://proxyccc.ccc:1234',
        'https_proxy': 'https://proxyccc.ccc:1233'
    }

    urls = requests.get('http://footballitarin.com/links.php')
    urls.raise_for_status()
    baseurl ='http://footballitarin.com/link_page.php'

    newsfile = 'C:\\Users\\paarsa\\Desktop\\footbalitarin_latest_news.html'
    data = urls.text
    #print(data)
    soup = BeautifulSoup(data, features='lxml')
    latestNews = soup.find_all('div', {'class': 'news_title'})
    # print(f'the length is {len(latestNews)}')
<<<<<<< HEAD
    with open(newsfile, 'w', encoding="utf-8") as f:
        for l in latestNews:
=======
    with open('/Users/asgarh/Desktop/'+fname+'.html', 'w') as f:
        for _ in latestNews:
>>>>>>> a764ef882230d0a2894bbf75cc790a6dd8e35256
            for news in latestNews:
                # print(news)
                for n in news:
                    # print(n)
                    #str(n).replace('link_page.php', baseurl)
                    f.write("<li>" + str(n).replace('link_page.php', baseurl) + "</li>")
    print('Successfully received the latest news from Footbalitarin Website!\n\n')
<<<<<<< HEAD
"""
    with open(newsfile, 'r', encoding='utf-8') as f:
        for a in f:
            print(a)
"""
=======

    with open('/Users/asgarh/Desktop/'+fname+'.html', 'r') as f:
            for _ in f:
                pprint(_)


>>>>>>> a764ef882230d0a2894bbf75cc790a6dd8e35256
getootbalitarinatestews()
