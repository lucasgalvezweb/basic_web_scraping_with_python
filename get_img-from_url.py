import requests
from bs4 import BeautifulSoup

urls_list = [
    "http://infosegura.web/2023/02/01/analysis-on-homicidal-violence-in-belize-2022/",
    "http://infosegura.web/2023/02/01/analisis-sobre-la-situacion-de-los-homicidios-en-belice-2022/",
    "http://infosegura.web/2023/01/27/analisis-sobre-la-violencia-homicida-en-guatemala-2022/",
    "http://infosegura.web/2023/01/27/logros-y-retos-para-seguir-impulsando-politicas-de-seguridad-ciudadana-centradas-en-las-personas/",
    "http://infosegura.web/2023/01/18/analisis-sobre-la-situacion-de-la-violencia-y-seguridad-ciudadana-en-honduras-2022/",
    "http://infosegura.web/2023/01/18/analisis-de-homicidios-y-seguridad-ciudadana-en-honduras-2022/",
    "http://infosegura.web/2023/01/18/los-homicidios-suben-por-segundo-ano-consecutivo-en-guatemala/",
    "http://infosegura.web/2023/01/16/violencia-homicida-en-guatemala-enero-a-septiembre-2022/",
    "http://infosegura.web/2023/01/16/homicidal-violence-guatemala-january-september-2022/",
    "http://infosegura.web/2023/01/16/analisis-sobre-homicidios-dolosos-en-costa-rica-enero-septiembre-2022/",
    "http://infosegura.web/2023/01/16/homicides-in-costa-rica-january-september-2022/",
    "http://infosegura.web/2023/01/12/tres-datos-positivos-para-comenzar-el-ano/"
]


def getImgURL(url):
    requestToPage = requests.get(url)
    soup = BeautifulSoup(requestToPage.text, 'html.parser')
    clases_md_12 = soup.find_all('div', class_='col-md-12')
    img_tag = clases_md_12[0].find('img')
    if img_tag != None:
        # print(img_tag)
        url_img_portada = img_tag.get('src')
        print(url_img_portada)


for url in urls_list:
    getImgURL(url)
