import requests
from bs4 import BeautifulSoup
import csv

def scrape_autotrader_data():
    url = "https://www.autotrader.com/cars-for-sale/cars-under-24000/honda/odyssey/roanoke-tx?isNewSearch=true&maxMileage=150000&searchRadius=0&startYear=2018&trimCodeList=ODYSSEY%7CEX-L%2CODYSSEY%7CElite%2CODYSSEY%7CTouring%2CODYSSEY%7CTouring%20Elite&zip=76262"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)

    autotrader_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        car_listings = soup.find_all('div', class_='inventory-listing')

        for car in car_listings:
            title_tag = car.find('h3', class_='text-bold')
            title = title_tag.get_text().strip() if title_tag else 'No Title'

            price_tag = car.find('span', class_='first-price')
            price = price_tag.get_text().strip() if price_tag else 'No Price'

            mileage_tag = car.find('span', class_='text-bold')
            mileage = mileage_tag.get_text().strip() if mileage_tag else 'No Mileage'

            link_tag = car.find('a', {'data-cmp': 'link'})
            link = 'https://www.autotrader.com' + link_tag['href'].strip() if link_tag else 'No URL'

            autotrader_data.append([title, price, mileage, link])

    else:
        print(f"Error: {response.status_code} - Unable to fetch data from AutoTrader.")

    return autotrader_data