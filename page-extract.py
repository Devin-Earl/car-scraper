import requests
import uuid
import random

# URL of page to extract
url = "https://dallas.craigslist.org/search/dallas-tx/cta?auto_make_model=honda%20odyssey&lat=32.7833&lon=-96.8&max_auto_miles=190000&max_auto_year=2024&max_price=25000&min_auto_miles=0&min_auto_year=2017&min_price=800&search_distance=410#search=1~gallery~0~4"

# Extended list of User-Agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
    user_agent = random.choice(user_agents)

headers = {
    "User-Agent": user_agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",  # Do Not Track Request Header
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
    
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    file_name = f'extracted-page_{uuid.uuid4()}.html'


    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f"HTML content saved to {file_name}")
else:
    print(f"Error: {response.status_code} - Unable to fetch data from Site.")