from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

url = input('http://www.dr-chuck.com/pageq.htm')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# retrieves all of the anchor tagsdd
# The TCP/IP gives us pipes / sockets between applications
# We designed application protocols to make use of these pipes
