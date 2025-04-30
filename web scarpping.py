import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
if response.status_code == 200:
    print("website fetched successfully!")
else:
    print("website fetched failed!")
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='text')
for quote in quotes:
    print(quote.text)
