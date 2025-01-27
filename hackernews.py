# fetches the last 10 news from news.ycombinator.com (hackernews)
# libs: beautiful soup 4 (bs4 package), requests
# para delimitar o numero de artigos, altere o parametro N da função get_text()

import requests
from bs4 import BeautifulSoup
from datetime import date


# funcoes
def get_text(n):
  cnt = 0

  span_list = soup.find_all("span", {"class": "titleline"})

  for span in span_list:
    link = span.find("a")  # Acha <a> dentro de span
    print(f"{span.text}")  # Texto do span
    print("\n")
    print(f"{link['href']}")  # URL do link

    cnt = cnt + 1 
    if cnt == n:  # Numero de Noticias
      break  # Interrompe o loop 'for' se cnt for maior que valor especificado (n)

#

t = date.today()
print("HackerNews - ", t)
print("\n")

site = requests.get("https://news.ycombinator.com/")
html = site.text
soup = BeautifulSoup(html, 'html.parser')

get_text(5)
