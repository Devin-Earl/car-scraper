import requests
from bs4 import BeautifulSoup
import csv

def extract_craigslist_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching the page: Status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all listings in the HTML
    listings = soup.find_all('li', class_='cl-static-search-result')
    
    car_listings = []
    for listing in listings:
        title_tag = listing.find('div', class_='title')
        price_tag = listing.find('div', class_='price')
        location_tag = listing.find('div', class_='location')
        link_tag = listing.find('a', href=True)

        title = title_tag.get_text().strip() if title_tag else 'No Title'
        price = price_tag.get_text().strip() if price_tag else 'No Price'
        location = location_tag.get_text().strip() if location_tag else 'No Location'
        link = link_tag['href'] if link_tag else 'No Link'

        car_listings.append([title, price, location, link])

    return car_listings

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Location', 'Link'])
        writer.writerows(data)
        print(f"Data has been written to {file_name}")

# URL of the Craigslist page
url = "https://dallas.craigslist.org/search/dallas-tx/cta?auto_make_model=honda%20odyssey&lat=32.7833&lon=-96.8&max_auto_miles=190000&max_auto_year=2024&max_price=25000&min_auto_miles=0&min_auto_year=2017&min_price=800&search_distance=410#search=1~gallery~0~100"  # Replace with the actual URL

# Extract car data
car_data = extract_craigslist_data(url)

# Save to CSV
if car_data:
    save_to_csv(car_data, 'craigslist_car_listings.csv')
else:
    print("No car data extracted")