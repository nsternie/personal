import HTMLParser
import requests

# APOD archive index page
index = requests.get('https://apod.nasa.gov/apod/archivepix.html')

parser = HTMLParser()
parser.feed()