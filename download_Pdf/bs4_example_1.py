# https://www.kdnuggets.com/web-scraping-fundamentals-for-data-science

# SCRAPE:  http://quotes.toscrape.com/
#               !
#               Get URL webpage response (requests.get)
#                   Parse response as HTL (BeautifulSoup)
#                       Find all quote containers
from bs4 import BeautifulSoup
import requests
import csv

# Making a GET request to the webpage to be scraped
page_response = requests.get("http://quotes.toscrape.com")

# Check if the GET request was successful before parsing the data
if page_response.status_code == 200:
    soup = BeautifulSoup(page_response.text, "html.parser")

    # Find all quote containers
    quote_containers = soup.find_all("div", class_="quote")
    
    # Lists to store quotes and authors
    quotes = []
    authors = []

    # Loop through each quote container and extract the quote and author
    for quote_div in quote_containers:
        # Extract the quote text
        quote = quote_div.find("span", class_="text").text
        quotes.append(quote)
        
        # Extract the author
        author = quote_div.find("small", class_="author").text
        authors.append(author)
    
    # Combine quotes and authors into a list of tuples
    data = list(zip(quotes, authors))

    # Save the data to a CSV file
    save_csv="bs4_example_1_quotes.csv"
    with open(save_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Quote", "Author"])
        # Write the data
        writer.writerows(data)
    
    print(f"Data saved to {save_csv}")
else:
    print(f"Failed to retrieve the webpage. Status code: {page_response.status_code}")


