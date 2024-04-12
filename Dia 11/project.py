import bs4, requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
# response = requests.get(url_base.format(15))
for n in range(1,11):
    response = requests.get(url_base.format(n))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    books = soup.select('.product_pod')
    book_list = {}
    for book in books:
        if book.select('.star-rating.Three') or book.select('.star-rating.Four') or book.select('.star-rating.Five'):
            book_list[book.select('h3')[0].getText()] = \
                {
                    "name" : book.select('h3')[0].getText(),
                    "price": book.select('.price_color')[0].getText()
                }

print(book_list)