import requests
from bs4 import BeautifulSoup
import urllib.request

# the url of the webpage containing the video
url = 'https://example.com/'

# send a GET request to the webpage
response = requests.get(url)

# parse the HTML using beautifulsoup
soup = BeautifulSoup(response.text, 'html.parser')

# find the video tag and get the source URL
video_tag = soup.find('video')
video_url = video_tag['src']

# download the video using urllib
urllib.request.urlretrieve(video_url, 'video.mp4')
