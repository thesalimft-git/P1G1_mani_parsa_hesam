

import pandas as pd

data = {
    'name': ['iphone', 'macbook', 'modem', 'samsung'],
    'price': [100, 150, 30, 80],
    'type': ['mobile', 'pc', 'craft', 'mobile'],
    'color': ['black', 'silver', 'white', 'blue']
}

df = pd.DataFrame(data)

# print(df[df['type'] == 'mobile'])
# print(df[df['price'] < 100]['name'])

