import pandas as pd

new = pd.read_csv('liberty.csv')

newer = new.set_index('book_name')['prices'].to_dict()

for keys in newer:
    if 'zorba' in keys:
        print(newer[keys])

