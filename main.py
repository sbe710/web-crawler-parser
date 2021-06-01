import requests
import re
from bs4 import BeautifulSoup

class Prodcut:
    name = str
    price = str
    link = str

    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link

    def __repr__(self):
        return str(self.__dict__)

headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

session = requests.session()
site = 'https://www.macmillandictionary.com/open-dictionary/index-chronological-order_page-1.htm'
response = session.get(site, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# for element in soup.find_all('div', class_='collection-product'):
#     name = element.find('h1', class_="product-card__title").text.strip()
#     price = element.find('span', class_="product-card__price").text.strip()
#     link = "https://kith.com/" + element.find('a').get('href')
#
#     prodcut = Prodcut(name, price, link)
#
#     print(prodcut.__repr__())



for element in soup.find_all('div'):
    print(element.text)

images = soup.findAll('img')
for image in images:
    #print image source
    print('Image:     ' + image['src'])

# img_tags = soup.find_all('img')
#
# urls = [img['src'] for img in img_tags]

#
# for url in urls:
#     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
#     if not filename:
#          print("Regex didn't match with the url: {}".format(url))
#          continue
#     with open(filename.group(1), 'wb') as f:
#         if 'http' not in url:
#             # sometimes an image source can be relative
#             # if it is provide the base url which also happens
#             # to be the site variable atm.
#             url = '{}{}'.format(site, url)
#         response = requests.get(url)
#         f.write(response.content)