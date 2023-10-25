import requests 
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

names = soup.find_all(name="a", class_="title")
prices = soup.find_all(name="h4", class_="pull-right price")
reviews = soup.find_all(name="p", class_="pull-right")

product_name = [titles.getText() for titles in names]
product_links = [titles.get("href") for titles in names]
product_prices = [price.getText() for price in prices]
product_reviews = [review.getText() for review in reviews]

column_names = ["Links", "Name", "Price", "Reviews"]
table = [[product_links, product_name, product_prices, product_reviews]]

df = pd.DataFrame({
    "Product Names": product_name,
    "Prices": product_prices,
    "Reviews": product_reviews,
    "Links": product_links
})

df.to_json("product_details.json", indent=4)
