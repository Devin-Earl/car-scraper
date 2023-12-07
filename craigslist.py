import requests
from bs4 import BeautifulSoup

def extract_craigslist_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching the page: Status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', class_='cl-static-search-result')

    craigslist_data = []
    for listing in listings:
        title_tag = listing.find('div', class_='title')
        price_tag = listing.find('div', class_='price')
        location_tag = listing.find('div', class_='location')
        link_tag = listing.find('a', href=True)

        title = title_tag.get_text().strip() if title_tag else 'No Title'
        price = price_tag.get_text().strip() if price_tag else 'No Price'
        location = location_tag.get_text().strip() if location_tag else 'No Location'
        link = link_tag['href'] if link_tag else 'No Link'

        craigslist_data.append([title, price, location, link])

    return craigslist_data
    