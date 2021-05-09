import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    information = soup.find_all('div', class_='latestListItem')
    news = []
    for info in information:
        try:
            title = info.find('h3', class_='ListItemHeading').find('a').text
        except:
            title = ''
        try:
            image = info.find('div', class_='ListItemThumbnail').find('img').get('data-src')
        except:
            image = ''

        if title == '':
            continue
        data = {
            'title': title,
            'image': image,
            'link': 'https://www.lonelyplanet.com/articles/alaska-traveler-vaccinations',
        }
        news.append(data)
    return news


def main():
    url = 'https://www.lonelyplanet.com/'
    return get_page_data(get_html(url))
