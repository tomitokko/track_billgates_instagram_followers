import requests
from bs4 import BeautifulSoup

user = "thisisbillgates"
url = 'https://www.instagram.com/'+ user
r = requests.get(url)
soup = BeautifulSoup(r.content)
followers = soup.find('meta', {'name': 'description'})['content']
follower_count = followers.split('Followers')[0]
print(follower_count)
