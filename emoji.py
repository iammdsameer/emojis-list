import requests
from bs4 import BeautifulSoup

URL = 'https://unicode.org/emoji/charts/full-emoji-list.html'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

f = open('./emojis.list', 'w')

for tr in soup.find_all('tr'):
    if tr.td != None:
        emoji = tr.find('td', class_='chars').text
        desc = tr.find('td', class_='name').text
        code = tr.find('td', class_='code').a.text
        f.write(emoji + '\t' + desc + '\t' + code + '\n')

f.close()
