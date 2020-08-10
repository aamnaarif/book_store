import requests
from requests_html import HTML
import pandas as pd
import time




page_num = 177




liberty_pages = []
liberty_authors = []
liberty_book_names = []
liberty_prices = []
liberty_descriptions = []

def make_pages(page_num):

    for i in range(1, page_num + 1):
        url = 'https://www.libertybooks.com/index.php?route=product/category&path=163#/sort=p.product_id/order=DESC/author=All/limit=25/page={}'.format(
            i)
        url_2 = 'https://www.libertybooks.com/index.php?route=product/category&path=163#/sort=p.product_id/order=DESC/author=All/limit=25/page=2'
        liberty_pages.append(url)
    return liberty_pages





def get_info(liberty_pages):
    count = 0
    for url in liberty_pages:
        page = requests.get(url)
        time.sleep(10)
        if page.status_code == 200:

            information = HTML(html=page.text)
            books_info_all = information.find('.main-products')
            # print(books_info_all[0].text)
            books_info = books_info_all[0].find('.product-details')
            for books in books_info:
                author_name = books.find('.author')
                for names in author_name:
                    # print(names.text + '\n')
                    liberty_authors.append(names.text[4::])
                name_of_books = books.find('.name')
                for book in name_of_books:
                    if book.text[4::] not in liberty_authors:
                        book_lower = book.text.lower()
                        if ' - paperback' in book_lower:
                            book_lower = book_lower.replace(' - paperback', '')
                            liberty_book_names.append(book_lower)
                        elif ' - (hb)' in book_lower:
                            book_lower = book_lower.replace(' - (hb)', '')
                            liberty_book_names.append(book_lower)
                        elif '- hardcover' in book_lower:
                            book_lower = book_lower.replace('- hardcover', '')
                            liberty_book_names.append(book_lower)
                        elif ' - (mmpb)' in book_lower:
                            book_lower = book_lower.replace(' - (mmpb)', '')
                            liberty_book_names.append(book_lower)
                        elif ' [paperback]' in book_lower:
                            book_lower = book_lower.replace(' - (mmpb)', '')
                            liberty_book_names.append(book_lower)
                        elif ' - (tpb)' in book_lower:
                            book_lower = book_lower.replace(' - (tpb)', '')
                            liberty_book_names.append(book_lower)
                        elif ' - (pb)' in book_lower:
                            book_lower = book_lower.replace(' - (pb)', '')
                            liberty_book_names.append(book_lower)


                        else:
                            liberty_book_names.append(book_lower)

                book_price = books.find('.price-tax')
                for price in book_price:
                    comma_price = price.text[11:].replace(',', '')
                    liberty_prices.append(float(comma_price))
                book_description = books.find('.description')
                for description in book_description:
                    liberty_descriptions.append(description.text)
                count += 1



""""
data = {'book_name': book_names, 'authors': authors, 'prices': prices,
        'description': descriptions}

df2 = pd.DataFrame(data)
new_df2 = df2.sort_values('book_name')
new_df2.to_csv('liberty_book.csv', index = False)
"""

if __name__ == "__main__":
    make_pages(page_num)
    print(liberty_pages)
    get_info(liberty_pages)
    data = {'book_name': liberty_book_names, 'authors': liberty_authors, 'prices': liberty_prices,
            'description': liberty_descriptions}
    df2 = pd.DataFrame(data)
    new_df2 = df2.sort_values('book_name')
    new_df2.to_csv('liberty.csv', index = False)













