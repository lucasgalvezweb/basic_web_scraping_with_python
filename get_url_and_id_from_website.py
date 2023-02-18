import requests
from bs4 import BeautifulSoup
from urllib import parse

url = 'http://127.0.0.1:5502/pag4.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

cuerpo_tabla = soup.find('tbody', id='the-list')
fila = cuerpo_tabla.find_all('tr')

for item in fila:
    columna_titulo = item.find('td', class_='title')
    edit_url = columna_titulo.find('a').get('href')
    # ID
    post_id = parse.parse_qs(parse.urlparse(edit_url).query)['post'][0]
    # URL
    div_url = columna_titulo.find('div', class_='row-actions')
    span_url = div_url.find('span', class_='view')
    url = span_url.find('a').get('href')

    print(post_id + ';' + url)
