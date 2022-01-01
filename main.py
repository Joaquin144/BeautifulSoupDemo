import requests
from bs4 import BeautifulSoup

# Get the website as HTML  :-------------
url = "http://codewithharry.com"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Parse the HTML  :-------------
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# HTML Tree Traversal  :-------------
# Types of objets -> TAG, NavigableString, BeautifulSoup, Comment
title = soup.title
# print(type(title))
# print(type(soup))

# get all paragraphs from webpage
paras = soup.findAll('p')
# print(paras)

# get all anchor tags from webpage
anchors = soup.findAll('a')
# print(anchors)

# Get first element
# print(soup.find('p'))

# Get first element ki class
# print(soup.find('p')['class'])

# Get all elements with class : lead
# print(soup.findAll("p", class_="lead"))


# get text from tags/soups
# print(soup.find('p').get_text())

# Get all the links on the webpage
# for link in anchors:
#     print(link.get('href'))

# A better practice to get all links is to store them in a set/list
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)