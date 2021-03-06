#!/usr/bin/env python
# coding: utf-8

# In[169]:


# Dependencies and Libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import pandas as pd
import requests
import regex as re
import json

#--------------------------------------------------------------

#                        Scraping Fuction
#--------------------------------------------------------------

def scrape_info():

    # Set up Splinter
    # Choose the executable path to driver for MAC users
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Visit visitcostarica.herokuapp.com
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the news title and news paragraph
    news_title = soup.find('div',class_='content_title').text

    # Paragraph
    parag= soup.find('div',class_='article_teaser_body').text

    # Save title and paragraph in dictionary mars
    mars_info={}
    mars_info["news_title"]= news_title
    mars_info["news_paragraph"]= parag

    mars_info

    url =  'https://spaceimages-mars.com/'
    browser.visit(url)

    # Find and click the full image button
    full_image= browser.find_by_tag('button')[1]
    full_image.click()

    # Scrape page into Soup
    html_image = browser.html
    soup = bs(html_image, "html.parser")

    # JPL Mars Space Images - Featured Image
    relative_image_path = soup.find('img', class_='fancybox-image').get('src')

    #Joining the URL of the page + the URL of the image
    featured_image_url= url + relative_image_path


    # Save image feature in dictionary mars
    mars_info["featured_image"]= featured_image_url

    #Printing the directory
    mars_info

    # Visit visitcostarica.herokuapp.com
    url =  'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Use Panda's read_html to parse the url
    mars_facts_table = pd.read_html(url, match='Equatorial Diameter')

    # Find the mars facts DataFrame in the list of DataFrames and assign it to mars_df
    mars_df = mars_facts_table[0]

    # Assign the columns Category, Value
    mars_df.columns = ['Category','Value']

    # Set the index to the 'Category' column without row indexing
    mars_df.set_index('Category', inplace=True)

    # Save html code to folder Assets
    mars_df.to_html()

    data = mars_df.to_dict(orient='records')

    # Save Data
    mars_info['facts_table']= mars_df


    #Printing dict
    mars_df


    url =  'https://marshemispheres.com/'
    browser.visit(url)
    # Html Object
    html = browser.html 

    # Parse HTML with Beautiful Soup
    soup=bs(html, 'html.parser')

    # Create a list for the full images url's
    hemispheres_img_urls = []

    # Retrieve all items that contain mars hemispheres inform action
    items = browser.find_by_css('a.product-item img')

    ## Looping throught the links (items), click the link, find the sample anchor
    # return the href


    for x in range(len(items)):
        
        hemispheres={}
        
        full_image_item = browser.find_by_tag('h3')[x]
        full_image_item.click()
        html= browser.html
        img_soup= bs(html, 'html.parser')
        # Finding the samplae image anchor tag and extact the href
        img= img_soup.find('a', text= 'Sample').attrs['href']
        full_img = f'{url}{img}'
        
        
        # Get Hemisphere title
        title = img_soup.find('h2', class_='title').get_text()
        # Append hemisphere object to list
        hemispheres['title'] = title
        hemispheres['img_url'] = full_img
        hemispheres_img_urls.append(hemispheres)
        
        # We need to go back
        browser.back()
        
    mars_info['hemispheres']= hemispheres_img_urls
    
    # Quit the browser
    browser.quit()
    return mars_info
