import requests
from bs4 import BeautifulSoup
import pandas as pd

course_title = []
teacher = []
course_price = []

with open('result.txt', 'w', encoding='utf-8') as f:
    for page in range(1, 6):
        path = f"https://toplearn.com/courses?pageId={page}"
        result = requests.get(path)

        soup = BeautifulSoup(result.text, 'html.parser')
        
        for h2tag in soup.find_all('h2'):
            for atag in h2tag.find('a'):
                course_title.append(atag)


        for div_top in soup.find_all('div', class_="top"):
            for atag in div_top.find('a'):
                # print(atag.text.strip())
                teacher.append(atag.text.strip())
        
        
        for span_price in soup.find_all('span', class_="price"):
            for itag in span_price.find('i'):
                print(itag.text)
                course_price.append(itag.text)


print('course_title: ', len(course_title))            
print('teacher: ', len(teacher))            
print('course_price: ', len(course_price))            




df = pd.DataFrame({
    'title': course_title,
    'teacher': teacher,
    'price': course_price
})

print(df)

