
Python News Headlines Scraper

This is a Python script to scrape top news headlines from a news website and save them into a text file.

Features

- Fetches HTML content from a specified news website URL
- Extracts headlines within <h1>, <h2>, and <h3> tags using BeautifulSoup
- Saves the headlines in a .txt file for easy reading and use

Requirements

- Python 3.x
- requests library
- beautifulsoup4 library

You can install the required libraries using:

bash
pip install requests beautifulsoup4


Usage

1. Set the target URL by modifying the URL variable in the script.
2. Run the script:

bash
python news_scraper.py


3. The headlines will be saved to headlines.txt (or the specified file name).

Example


10 headlines saved to headlines.txt


