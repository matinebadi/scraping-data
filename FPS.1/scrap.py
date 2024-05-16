
from bs4 import BeautifulSoup
import requests

def GetUrls():
    url = 'https://jeetel.com/all-product/bar-asaas-model-mobile/all-headset-wireless'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    return [tag['href'] for tag in soup.find_all('a', class_='title')]


def GetDatas():
    AllProduct = []
    for url in GetUrls():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        text = (soup.find('a', class_='title')).text
        price = (soup.find('span', id='ProductPrice'))['data-price']
        catdiv = soup.find('div', class_='breadcrumbs clearfix')
        category = [tag.text for tag in catdiv.findAll('a')][-1]
        discount = (soup.find('div', class_='discount')).find('span').text
        description = (soup.find('div', class_='text-area')).find('p').text
        available = (soup.find('div', class_='d-flex justify-content-start align-items-center box-custom mt-2 py-2 status-box')).find('span').text

        AllProduct.append({
            'name': text,
            'link': url,
            'price': price,
            'category': category,
            'discount': discount,
            'available': available,
            'description': description
        })
    return AllProduct
