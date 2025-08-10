# web scraper for news headlines...........

import requests
from bs4 import BeautifulSoup

# News URL to scrape
URL = 'https://www.indiatoday.in/'

# Send a GET request to the URL
response = requests.get(URL)
response.raise_for_status()  # Check for request errors

soup = BeautifulSoup(response.text, 'html.parser')

# Find all the news headlines
headlines = soup.find_all('h2')  # Adjust the tag and class as needed

# Save headlines to a file
with open('headlines.txt', 'w', encoding='utf-8') as f:
    for headline in headlines:
        headline = headline.get_text(strip=True)
        # Write each headline text to the file
        f.write(headline + '\n \n')

print(f"Scraped {len(headlines)} headlines from {URL} and saved to 'headlines.txt'.")
# Note: Ensure you have the required libraries installed:
# pip install requests beautifulsoup4

