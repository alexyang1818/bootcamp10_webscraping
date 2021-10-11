# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # scrape articles


# visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page
# searching for elements with a specific combination of tag (div) and attribute (list_text)
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') # select_one selects the first one. same as find()


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


news_summary = slide_elem.find('div', class_='article_teaser_body').get_text()
news_summary


# # scrape images from another website
# 

# visit url
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


img_url = url + img_url_rel
img_url
# browser.visit(img_url)


# # scrape Mars facts


# use pandas to extract table contents. the url has two tables

df = pd.read_html('https://galaxyfacts-mars.com')[0]  # create df from the first html table
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df.head()


df2 = pd.read_html('https://galaxyfacts-mars.com')[1]  # create df from the second html table
df2.head()


df.to_html()


browser.quit()
