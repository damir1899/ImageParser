from json import dump, load
from os import getenv, system 
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
system('clear')

URL = getenv('URL')
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

def get_html(search, header):
    response = requests.get(url=f'https://www.wallpaperflare.com/search?wallpaper={search}', headers=header)
    if response.status_code == 200:
        return response.text
    else:
        return f'Ошибка {response.status_code}'
    

# with open('core/html/index.html', 'w') as file:
#     file.write(str(get_html(URL, HEADERS)))

def get_response(html):
    soup = BeautifulSoup(html, 'lxml').find('ul', {'class': 'gallery', 'id': 'gallery'}).find_all('img')
    
    src = {}
    for item in soup:
        image = item.get('data-src')
        caption = item.get('alt')
        src.update({
            caption: image
        })
        
    return src


def url_parser(search):
    html = get_html(search, HEADERS)
    soup = get_response(html)
    with open('core/json/content.json', 'w', encoding='UTF-8') as file:
        dump(soup, file, indent=4, ensure_ascii=False)

url_parser('marvel')
    

    