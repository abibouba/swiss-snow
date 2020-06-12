import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from .Resort import Resort


def parse_website_verbier():
    # Set the URL
    url_verbier = "http://www.infosnow.ch/~apgmontagne/?lang=en&pid=31"

    # Parse the html
    page = requests.get(url_verbier)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Create the resort status object
    verbier = Resort()
    verbier.name = "Verbier - 4 vallées"

    # Get the last updated date
    html_update = soup.find_all('div')[3].text
    verbier.last_update = datetime.strptime(re.sub('Last changes: ', '', html_update), '%d.%m.%Y %H:%M')

    # Get the avalanche risk level
    verbier.avalanche_level = soup.find_all('td')[32].text

    # Get the slopes stats
    html_slopes = soup.find_all('h1')[1].text
    verbier.slopes_open = re.findall(r'\d+', html_slopes)[0]
    verbier.slopes_total = re.findall(r'\d+', html_slopes)[1]

    # Get the lifts stats
    html_lifts = soup.find_all('td')[35].text
    verbier.lifts_open = re.findall(r'\d+', html_lifts)[0]
    verbier.lifts_total = re.findall(r'\d+', html_lifts)[1]

    # Get the snow conditions
    html_snow = soup.find_all('table')[3]
    verbier.add_condition(location=html_snow.contents[0].contents[1].text,
                          altitude=html_snow.contents[0].contents[3].text,
                          snow_height=html_snow.contents[0].contents[5].text,
                          snow_fresh=html_snow.contents[0].contents[7].text)
    verbier.add_condition(location=html_snow.contents[1].contents[1].text,
                          altitude=html_snow.contents[1].contents[3].text,
                          snow_height=html_snow.contents[1].contents[5].text,
                          snow_fresh=html_snow.contents[1].contents[7].text)
    verbier.add_condition(location=html_snow.contents[2].contents[1].text,
                          altitude=html_snow.contents[2].contents[3].text,
                          snow_height=html_snow.contents[2].contents[5].text,
                          snow_fresh=html_snow.contents[2].contents[7].text)

    return verbier
