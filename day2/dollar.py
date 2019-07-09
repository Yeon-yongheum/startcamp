# 0. 활용할 패키지를 불러온다.
import requests
from bs4 import BeautifulSoup
# 1. url을 설정한다.
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청을 보내고, 그 결과의 내용을(text) response에 저장한다.
response = requests.get(url).text
# 3. html 문서로 변환한다.
soup = BeautifulSoup(response,'html.parser')
# 4. 원하는 값을 선택자(selector)를 활용해서 가져온다.
table = soup.select('body > div > table > tbody > tr')
dollar = soup.select ('body > div > table > tbody > tr:nth-child(1) > td.sale')
for tr in table : 
    print(tr.select('td.sale'))
    print(tr.select_one('td.sale').text)

print(dollar)
# print(type(table))