import requests
from bs4 import BeautifulSoup

def search_keyword(keyword):
    yahoo_url = f"https://search.yahoo.com/search?p={keyword}"
    yahoo_response = requests.get(yahoo_url)
    yahoo_soup = BeautifulSoup(yahoo_response.text, 'html.parser')
    yahoo_results = yahoo_soup.select('.algo')
    yahoo_data = [{'title': result.find('a').text, 'url': result.find('a')['href']} for result in yahoo_results]
    return yahoo_data[:30]

keyword = input("Enter the keyword: ")
results = search_keyword(keyword)

# Printing the titles and URLs vertically
for index, result in enumerate(results, start=1):
    print(f"--- Result {index} ---")
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print("-------------------")
