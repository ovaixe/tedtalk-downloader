from bs4 import BeautifulSoup
import requests
import re
import sys


if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit('Error: Please enter the TED Talk URL')

resp = requests.get(url)

print('Download about to start.....')

soup = BeautifulSoup(resp.content, 'html.parser')
result = ''
for val in soup.find_all('script'):
    if re.search('talkPage.init', str(val)):
        result = str(val)

result_mp4 = re.search('(?P<url>https?://[^\s]+)(mp4)', result).group('url')

mp4_url = result_mp4.split(',')[2]
mp4_url =mp4_url.split('"')[3]

print('Downloading video from ....', mp4_url)

file_name = mp4_url.split('/')[len(mp4_url.split('/')) - 1].split('?')[0]

print('Storing video in .... ', file_name)

resp = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(resp.content)

print('Download Process finished.')
