# 객체 지향 언어
# 0. requests,bs4 패키지를 불러온다
# pip install requests:요청보내주는 패키지
# pip install bs4 : 문서를 첮기 편하게 바꿔주는 패키지 (파싱)
import requests
from bs4 import BeautifulSoup
# 1. url로 요청(requests.get)을 보내고, reponse로 저장
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text # print(response.text)# print(type(response.text))
# 2. 파이썬이 찾기 편한 형식으로 문서를 변경한다.
soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# print(type(response))
# print(type(soup))
# 3. KOSPI 값을 찾는다.
kospi = soup.select_one('#KOSPI_now').text
print(kospi)