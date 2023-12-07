import datetime
import os
import csv
from autotrader import scrape_autotrader_data
from craigslist import extract_craigslist_data

def standardize_data(autotrader_data, craigslist_data):
    # Standardize AutoTrader data by adding 'N/A' for location
    standardized_autotrader = [item + ['N/A'] for item in autotrader_data]

    # Standardize Craigslist data by inserting 'N/A' for mileage
    standardized_craigslist = [item[:2] + ['N/A'] + item[2:] for item in craigslist_data]

    return standardized_autotrader + standardized_craigslist

def combine_and_check_duplicates(combined_data, previous_file):
    if os.path.exists(previous_file):
        with open(previous_file, 'r', encoding='utf-8') as file:
            existing_data = list(csv.reader(file))
            for row in combined_data:
                if row in existing_data:
                    row.append('Duplicate')
                else:
                    row.append('New')
    else:
        combined_data = [row + ['New'] for row in combined_data]

    return combined_data

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Mileage', 'Location', 'Link', 'Status'])
        writer.writerows(data)

def main():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}_car_listings.csv"
    previous_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    previous_file = f"{previous_date}_car_listings.csv"

    autotrader_data = scrape_autotrader_data()
    craigslist_url = "https://dallas.craigslist.org/search/dallas-tx/cta?auto_make_model=honda%20odyssey&lat=32.7833&lon=-96.8&max_auto_miles=190000&max_auto_year=2024&max_price=25000&min_auto_miles=0&min_auto_year=2017&min_price=800&search_distance=410#search=1~gallery~0~100"
    craigslist_data = extract_craigslist_data(craigslist_url)

    standardized_data = standardize_data(autotrader_data, craigslist_data)
    combined_data = combine_and_check_duplicates(standardized_data, previous_file)
    save_to_csv(combined_data, filename)

if __name__ == "__main__":
    main()