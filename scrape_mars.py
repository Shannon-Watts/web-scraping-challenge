import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#NASA MARS NEWS
# Retrieve page 
url = "https://redplanetscience.com/"
browser.visit(url)

html = browser.html

# Create a Beautiful Soup object 
soup = bs(html, 'html.parser')

#soup.find_all("div", {"class": "content_title"})
news = soup.find('div', {"id": "news"})

all_news = []
for n in news.find_all("div", class_="content_title"):
    try:
        all_news.append(n.text)
    except:
        print("nothing to scrape")

all_articles = []
for n in news.find_all('div', class_='article_teaser_body'):
    try:
        all_articles.append(n.text)
    except:
        print("nothing to scrape")

## JPL MARS SPACE IMAGES 

# Use Splinter to navigate the site and find the image URL for the current Featured Mars Image
url_fi = "https://spaceimages-mars.com"
browser.visit(url_fi)

html = browser.html

# Find link using splinter and click to find featured image
browser.links.find_by_partial_text('FULL IMAGE').click()


# Create a Beautiful Soup object 
fi_soup = bs(html, 'html.parser')

# Find URL of image and save as variable
featured_image_url = fi_soup.find("img")["src"]

featured_image_url


# show string
featured_image_url = f'https://spaceimages-mars.com/{featured_image}'

print(featured_image_url)

## MARS FACTS

# Usa Pandas to scrape table
url = 'https://galaxyfacts-mars.com/'

# Read the table
tables = pd.read_html(url)
tables

# See as df
df = tables[0]
df

# Clean df
new_header = df.iloc[0] #grab the first row for the header
df.columns = new_header 
df = df.iloc[1: , :]
df

# Convert data to HTML table string
html_table = df.to_html()
html_table

df.to_html('table.html')

## MARS HEMIS

#click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
browser.visit(url_MH)

html = browser.html

