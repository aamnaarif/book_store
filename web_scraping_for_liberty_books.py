from selenium.webdriver import Chrome
import pandas as pd
import time


webdriver = '/Users/aamnaarifkhan/Desktop/chromedriver'

driver = Chrome(webdriver)



liberty_pages = 176
liberty_book_names = []
liberty_book_authors = []
liberty_book_prices = []




for page in range(1,liberty_pages):


    url = 'https://www.libertybooks.com/index.php?route=product/category&path=163#/sort=p.product_id/order=DESC/author=All/limit=25/page={}'.format(page)

    driver.get(url)
    time.sleep(5)


    product_details = driver.find_elements_by_class_name("product-details")

    for product in product_details:
            book_name = product.find_element_by_class_name('name').text

            book_lower = book_name.lower()
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
            elif ' - (pb)' in book_lower:
                book_lower = book_lower.replace(' - (pb)', '')
                liberty_book_names.append(book_lower)


            else:
                liberty_book_names.append(book_lower)


            book_author = product.find_element_by_class_name('author').text[4:]
            liberty_book_authors.append(book_author)

            try:
                book_prices = \
                product.find_element_by_class_name('price').text.split()[3]
                book_price = book_prices.replace(',', '')

                liberty_book_prices.append(float(book_price))
            except:
                book_prices = \
                product.find_element_by_class_name('price').text.split()[1]
                book_price = book_prices.replace(',', '')

                liberty_book_prices.append(float(book_price))

    print(page)








driver.close()

data = {'book_name': liberty_book_names, 'authors': liberty_book_authors,
        'prices': liberty_book_prices}
df2 = pd.DataFrame(data)
new_df2 = df2.sort_values('book_name')
new_df3 = new_df2.drop_duplicates(subset= 'book_name').sort_values('book_name')
new_df3.to_csv('liberty.csv', index=False)

