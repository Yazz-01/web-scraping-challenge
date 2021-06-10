from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_mars():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import time\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from pprint import pprint\n",
    "import pandas as pd\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [/Users/yazminrodriguez/.wdm/drivers/chromedriver/mac64/91.0.4472.19/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Set up Splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### NASA Mars News\n",
    "Finding the title and paragraph from: https://redplanetscience.com/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit visitcostarica.herokuapp.com\n",
    "url = \"https://redplanetscience.com/\"\n",
    "browser.visit(url)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    " # Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # Get the average temps\n",
    "avg_temp= soup.find('div',class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Perseverance Rover 100 Days Out\""
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_temp.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars[\"news_title\"]= avg_temp.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Paragraph\n",
    "parag= soup.find('div',class_='article_teaser_body')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Mark your calendars: The agency's latest rover has only about 8,640,000 seconds to go before it touches down on the Red Planet, becoming history's next Mars car.\""
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parag.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars[\"news_paragraph\"]= parag.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'news_title': \"NASA's Perseverance Rover 100 Days Out\",\n",
       " 'news_paragraph': \"Mark your calendars: The agency's latest rover has only about 8,640,000 seconds to go before it touches down on the Red Planet, becoming history's next Mars car.\"}"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### JPL Mars Space Images - Featured Image\n",
    "Finding images from: https://spaceimages-mars.com/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit visitcostarica.herokuapp.com\n",
    "url =  'https://spaceimages-mars.com/'\n",
    "browser.visit(url)\n",
    "\n",
    " # Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars3.jpg'"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# JPL Mars Space Images - Featured Image\n",
    "\n",
    "relative_image_path = soup.find('img', class_='fade-in').get('src')\n",
    "\n",
    "#Joining the URL of the page + the URL of the image\n",
    "\n",
    "featured_image_url= 'https://spaceimages-mars.com/'+ relative_image_path\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars3.jpg'"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "relative_image_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# adding the image to Directory Mars\n",
    "\n",
    "mars['mars_images']=relative_image_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'news_title': \"NASA's Perseverance Rover 100 Days Out\",\n",
       " 'news_paragraph': \"Mark your calendars: The agency's latest rover has only about 8,640,000 seconds to go before it touches down on the Red Planet, becoming history's next Mars car.\",\n",
       " 'mars_images': 'image/featured/mars3.jpg'}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Printing the directory\n",
    "mars"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts\n",
    "Finding a table from: https://galaxyfacts-mars.com/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit visitcostarica.herokuapp.com\n",
    "url =  'https://galaxyfacts-mars.com/'\n",
    "browser.visit(url)\n",
    "\n",
    " # Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<table class=\"table table-striped\">\n",
       "<tbody>\n",
       "<tr>\n",
       "<th scope=\"row\">Equatorial Diameter:</th>\n",
       "<td>6,792 km</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Polar Diameter:</th>\n",
       "<td>6,752 km</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Mass:</th>\n",
       "<td>\t6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Moons:</th>\n",
       "<td>\t2 ( <span class=\"red\">Phobos </span> &amp; <span class=\"red\"> Deimos </span>)</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Orbit Distance:</th>\n",
       "<td>\t227,943,824 km (1.38 AU)</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Orbit Period:</th>\n",
       "<td>\t687 days (1.9 years)</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Surface Temperature:</th>\n",
       "<td>\t-87 to -5 °C</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">First Record:</th>\n",
       "<td>\t2nd millennium BC</td>\n",
       "</tr>\n",
       "<tr>\n",
       "<th scope=\"row\">Recorded By:</th>\n",
       "<td>\tEgyptian astronomers</td>\n",
       "</tr>\n",
       "</tbody>\n",
       "</table>"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scraping to get the table of facts\n",
    "\n",
    "table_facts= soup.find('table',class_='table table-striped')\n",
    "table_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 ( Phobos &amp; Deimos )</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:          2 ( Phobos & Deimos )\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use Panda's `read_html` to parse the url\n",
    "mars_facts = pd.read_html(url, match='Equatorial Diameter')\n",
    "\n",
    "# Find the mars facts DataFrame in the list of DataFrames and assign it to `mars_df`\n",
    "mars_df = mars_facts[0]\n",
    "\n",
    "mars_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Category</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 ( Phobos &amp; Deimos )</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Value\n",
       "Category                                           \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                        2 ( Phobos & Deimos )\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# Assign the columns Category, Value\n",
    "mars_df.columns = ['Category','Value']\n",
    "\n",
    "# Set the index to the `Description` column without row indexing\n",
    "mars_df.set_index('Category', inplace=True)\n",
    "\n",
    "# Save html code to folder Assets\n",
    "mars_df.to_html()\n",
    "\n",
    "data = mars_df.to_dict(orient='records')  # Here's our added param..\n",
    "\n",
    "# Display mars_df\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Hemispheres\n",
    "\n",
    "Obtaining high resolution images for each of Mar's hemispheres.https://marshemispheres.com/\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the website\n",
    "url =  'https://marshemispheres.com/'\n",
    "browser.visit(url)\n",
    "\n",
    " # Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Save both the image url string for the full resolution hemisphere\n",
    "#image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.\n",
    "\n",
    "# Retrieve all items with Mars Hemisphere info (4)\n",
    "relative_path = soup.find('div', class_='item')\n",
    "\n",
    "# Create empty list for hemisphere_image_urls\n",
    "hemisphere_image_urls=[]\n",
    "\n",
    "# Store in the list the main url\n",
    "main_url_hemisphere= 'https://marshemispheres.com/index.html'\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'items' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-144-5c08c7625884>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Loop through the items\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mitems\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m    \u001b[0;31m#Store title\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m    \u001b[0mtitle\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'h3'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'items' is not defined"
     ]
    }
   ],
   "source": [
    " #Loop through the items \n",
    "for i in items:\n",
    "    #Store title\n",
    "    title= i.find('h3').text\n",
    "    \n",
    "    #Store link that leads to full image website\n",
    "    img_url= i.find('a', class_='open_toggle')['href']\n",
    "    \n",
    "    #Open link with the full image\n",
    "    browser.visit(main_url_hemisphere + img_url)\n",
    "    \n",
    "    #HTML object of individual hemisphere information website\n",
    "    img_url_html = browser.html\n",
    "    \n",
    "    #Parse HTML with bs for each hemisphere information website\n",
    "    soup = bs(img_url_html, \"html.parser\")\n",
    "    \n",
    "    #Retrieve full image source\n",
    "    full_img_url= main_url_hemisphere + soup.find('img',class_= 'wide-image')['src']\n",
    "    \n",
    "    #Append this retrieved info to the list of dicts.\n",
    "    hemisphere_image_urls.append({'title':title, 'image_url':'full_img_url'})\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "   \n",
    "#Print hemisphere list of dicts.\n",
    "hemisphere_image_urls\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}