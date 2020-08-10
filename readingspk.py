import requests
from requests_html import HTML
import pandas as pd







url = 'https://www.readings.com.pk/pages/category.aspx?Category=13&Level=Level1&Sortby=ArrivalDate&BookType=N&Page=1'

readings_pages = []

#change the page numbers

page_num = 3256

readings_authors = []
readings_book_names = []
readings_prices = []





def make_readings_pages(page_num):
    for i in range(1, page_num + 1):
        new_url = 'https://www.readings.com.pk/pages/category.aspx?Category=&Level=&Sortby=ArrivalDate&BookType=&Page=1'.format(
            i)
        readings_pages.append(new_url)
    return readings_pages



def get_data(pages):
    count = 0
    for url in pages:
        page = requests.get(url)
        if page.status_code == 200:
            information = HTML(html=page.text)
            all_books_information = information.find(
                '#ContentPlaceHolder1_DL_Books')
            # print(all_books_information[0].text)
            books_info = all_books_information[0].find('td')
            for books in books_info:
                author_name = books.find('h6')
                readings_authors.append(author_name[0].text)
                intermediate = books.find('h5')
                book_name = intermediate[0].find('a')
                if book_name[0].text.endswith(':'):
                    readings_book_names.append(
                        book_name[0].text[0:len(book_name[0].text) - 1])
                else:
                    readings_book_names.append(book_name[0].text)

                book_price_total = books.find('.our_price')
                try:
                    book_price = book_price_total[0].find('span')
                    # print(book_price[3].text)
                    readings_prices.append(float(book_price[3].text[3::]))
                except:
                    book_price = book_price_total[0].find('span')
                    readings_prices.append(book_price[2].text)
        count += 1
        print(count)













if __name__ == "__main__":
    pages = make_readings_pages(page_num)
    get_data(pages)
    data = {'book_name': readings_book_names, 'authors': readings_authors, 'prices': readings_prices}
    df = pd.DataFrame(data)
    new_df = df.sort_values('book_name')











