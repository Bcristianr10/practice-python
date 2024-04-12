import bs4
import requests
url_blog  = 'https://escueladirecta-blog.blogspot.com/'
url_courses = 'https://www.escueladirecta.com/courses/'

response = requests.get(url_courses)
soup = bs4.BeautifulSoup(response.text,'lxml')
title = soup.select('title')[0].getText()
elements = soup.select('.course-box-image')
# images  = []

for element in elements:
    src = element['src']
    image = requests.get(src)
    file = open('my_image.jpg','wb')
    file.write(image.content)
    file.close()
    # images.append(src)


