import datetime
import os
import csv
from autotrader import scrape_autotrader_data
from craigslist import extract_craigslist_data

def standardize_data(autotrader_data, craigslist_data):
    valid_data = []
    invalid_data = []

    for item in autotrader_data:
        if len(item) == 4:  # Expected length for AutoTrader data
            valid_data.append(item + ['N/A'])  # Add 'N/A' for location
        else:
            invalid_data.append(item)

    for item in craigslist_data:
        if len(item) == 4:  # Expected length for Craigslist data
            valid_data.append(item[:2] + ['N/A'] + item[2:])  # Insert 'N/A' for mileage
        else:
            invalid_data.append(item)

    return valid_data, invalid_data

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

def save_to_csv(valid_data, invalid_data, file_name):
    base_name, ext = os.path.splitext(file_name)
    valid_file = base_name + ext
    invalid_file = base_name + '_invalid' + ext

    # Save valid data
    with open(valid_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Mileage', 'Location', 'Link', 'Status'])
        for row in valid_data:
            writer.writerow(row)

    # Save invalid data, if any
    if invalid_data:
        with open(invalid_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Data'])  # Adjust header based on actual data structure
            for row in invalid_data:
                writer.writerow([row])  # Adjust based on actual data structure

def main():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}_car_listings.csv"
    previous_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    previous_file = f"{previous_date}_car_listings.csv"

    autotrader_data = scrape_autotrader_data()
    craigslist_url = "https://dallas.craigslist.org/search/dallas-tx/cta?auto_make_model=honda%20odyssey&lat=32.7833&lon=-96.8&max_auto_miles=190000&max_auto_year=2024&max_price=25000&min_auto_miles=0&min_auto_year=2017&min_price=800&search_distance=410#search=1~gallery~0~100"
    craigslist_data = extract_craigslist_data(craigslist_url)

    valid_data, invalid_data = standardize_data(autotrader_data, craigslist_data)
    combined_data = combine_and_check_duplicates(valid_data, previous_file)
    save_to_csv(combined_data, invalid_data, filename)

if __name__ == "__main__":
    main()