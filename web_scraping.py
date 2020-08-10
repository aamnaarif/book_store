import requests
from requests_html import HTML
import pandas as pd

""""
information = HTML(html = page.text)
        categories = information.find('.side_categories')
        print(categories[1].text)"""


pages = []
prices = []
stars = []
titles = []
urls = []

url = 'http://books.toscrape.com/catalogue/page-1.html'
pages_to_scrape = 10


# create a list with all the pages we have to scrape
for i in range(1, pages_to_scrape+1):
    url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
    pages.append(url)
# go through the pages one by one and scrape them
for item in pages:
    page = requests.get(item)
    if page.status_code == 200:
         information = HTML(html = page.text)
         product_info = information.find(".product_pod")
         for i  in range(len(product_info)):
             all_info = product_info[i].text.split('\n')
             titles.append(all_info[0])
             prices.append(all_info[1])
             stars_info_dict = product_info[i].find('.star-rating')
             stars_info_attrs = stars_info_dict[0].attrs
             stars_info = stars_info_attrs['class'][1]
             stars.append(stars_info)

data  = {'titles':titles, 'price': prices, 'stars':stars}
df = pd.DataFrame(data = data)
df.to_csv('books.csv', index = False)











