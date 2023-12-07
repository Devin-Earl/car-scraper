Car Listings Data Aggregator

Overview

This project is a Python-based data aggregator that scrapes car listings from AutoTrader and Craigslist, combines the data, identifies duplicates, and generates a daily CSV file. It was born out of a desire to find a new minivan for a good friend after his wife totaled theirs 

Features

- Web Scraping: Extracts car listings data from AutoTrader and Craigslist.

- Data Standardization: Standardizes data from different sources for consistency.

- Duplicate Identification: Checks and marks duplicate entries based on historical data.

- CSV Generation: Outputs aggregated data into a CSV file.

- Error Handling: This is a Work In Progress ultimately this will only be used for a few days maybe a week so I didn't spend too much time here 

Installation

To set up this project, follow these steps:

1\. Clone the Repository:

git clone 

2\. Navigate to the Project Directory:

cd car-scraper

3\. Install Dependencies:

- Ensure Python 3.10 is installed.

- Install required Python packages:

pip install -r requirements.txt

Usage

To run the aggregator:

1\. Run the Main Script:

python main.py

1\. This will scrape data from AutoTrader and Craigslist, combine it, check for duplicates, and generate a CSV file named with the current date.

2\. CSV Files:

- The aggregated data is saved in YYYY-MM-DD_car_listings.csv.

- Malformed or unexpected data is saved in YYYY-MM-DD_car_listings_invalid.csv.

Files and Directories

- main.py: The main Python script to run the aggregator.

- autotrader.py: Module to scrape data from AutoTrader.

- craigslist.py: Module to scrape data from Craigslist.

- requirements.txt: List of Python packages required.

- page-extract.py Adhoc scraper module to help determine what specific tags and such BS4 needs to target. 


Additional Notes:

- This script contains little error handeling and may not produce 100% cleaned data truthfully this is simply made to help some good friends nothing more 

- Multiple values are hardcoded for simplicty sake, specifically the vehicle specifics feel free to dive into the python code and change values accordingly

- This was running locally using a CHRON job to execute it everyday at midnight I may use a Github Actions workflow to do this directly on the repository in the future 

- Requirements File: This README assumes you have a requirements.txt file listing all necessary Python packages. Create this file in your project if you haven't already.

