import requests
from bs4 import BeautifulSoup as bs

# Функция для парсинга страницы url. В выводе- цитата, автор, теги.
def quotes_test():
    url = "https://quotes.toscrape.com"
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    news = soup.find_all('span',class_='text')
    auths = soup.find_all('small',class_='author')
    tags = soup.find_all('div',class_='tags')
    for new in range(len(news)):
        print(news[new].getText()+'\n-'+auths[new].getText())
        tfq = tags[new].find_all('a',class_='tag')
        for tag in tfq:
            print('#' + tag.text)
        print('\n')

#Функция для парсинга страницы url(магазин с товарами). На выводе: номер лота, цена и наименование товара.
def scrapingclub_test():
    url = "https://scrapingclub.com/exercise/list_basic/?page=1"
    params = {'page':1}
    page = 2
    i = 1

    while params['page'] < page:
        r = requests.get(url)
        soup = bs(r.text,"html.parser")
        items = soup.find_all('div',class_="col-lg-4 col-md-6 mb-4")
        
        for i, it in enumerate(items,start=i):
            itemName = it.find('h4',class_='card-title').text.strip()
            itemPrice = it.find('h5').text.strip()
            print(f"{i}) {itemPrice} за {itemName}")

        lastpage = int(soup.find_all('a',class_='page-link')[-2].text) 
        page = lastpage if page < lastpage else page
        params['page'] += 1

        
quotes_test()
scrapingclub_test()