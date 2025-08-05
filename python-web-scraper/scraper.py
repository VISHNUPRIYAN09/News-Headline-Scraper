import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"  # Replace with your preferred news site
FILENAME = "headlines.txt"

# Step 1: Make a request to the URL
response = requests.get(URL)

# Check if the response status is OK (200)
if response.status_code != 200:
    print(f"Failed to retrieve content. HTTP Status Code: {response.status_code}")
else:
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find headlines within h1, h2, or h3 tags
    headlines = []
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        text = tag.get_text(strip=True)
        if text:  # Only append non-empty headlines
            headlines.append(text)

    # Step 4: Save the headlines to a .txt file
    with open(FILENAME, "w", encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline + "\n")

    # Step 5: Output the result
    print(f"{len(headlines)} headlines saved to {FILENAME}")