import requests
import bs4

response = requests.get('https://www.acmicpc.net/user/minjae2271').text
soup = bs4.BeautifulSoup(response,'html.parser')
correct = soup.select('#statics > tbody > tr > td > a')
my_id = soup.select('#body > div.wrapper > div.header.no-print > div.topbar > div > ul > li:nth-child(1) > a')
for title in correct:
    print(title.text)
for title in my_id:
    print(title.text)