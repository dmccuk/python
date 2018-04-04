# Import libraries
import requests
from bs4 import BeautifulSoup


# Collect first page of artists’ list
page = requests.get('https://github.com/opsmotion/terraform/blob/master/README.md')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
#list(soup.children)

