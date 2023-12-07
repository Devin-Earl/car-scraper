import requests
from bs4 import BeautifulSoup
import csv

# URL of AutoTrader search results page
url = "https://www.autotrader.com/cars-for-sale/cars-under-24000/honda/odyssey/roanoke-tx?isNewSearch=true&maxMileage=150000&searchRadius=0&startYear=2018&trimCodeList=ODYSSEY%7CEX-L%2CODYSSEY%7CElite%2CODYSSEY%7CTouring%2CODYSSEY%7CTouring%20Elite&zip=76262"

# Set a User-Agent header to avoid potential blocking
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all car listings
    car_listings = soup.find_all('div', class_='inventory-listing')

    # Open a CSV file to write to
    with open('car_listings.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Title', 'Price', 'Mileage', 'Link'])

        for car in car_listings:
            # Extract car title
            title_tag = car.find('h3', class_='text-bold')
            title = title_tag.get_text().strip() if title_tag else 'No Title'

            # Extract car price
            price_tag = car.find('span', class_='first-price')
            price = price_tag.get_text().strip() if price_tag else 'No Price'

            # Extract car mileage
            mileage_tag = car.find('span', class_='text-bold')
            mileage = mileage_tag.get_text().strip() if mileage_tag else 'No Mileage'

            # Extract car URL
            link_tag = car.find('a', {'data-cmp': 'link'})
            link = 'https://www.autotrader.com' + link_tag['href'].strip() if link_tag else 'No URL'

            # Write to CSV
            writer.writerow([title, price, mileage, link])

    print("Data has been written to car_listings.csv")

else:
    print(f"Error: {response.status_code} - Unable to fetch data from AutoTrader.")
