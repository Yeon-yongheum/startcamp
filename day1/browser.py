import webbrowser
import requests

idols = ['bts','iu','itzy']

for idol in idols :
    #string interpolation
    #문자열 보간법 : f-string / 파이썬 3.6이상에서 가능
    webbrowser.open(f'https://search.naver.com/search.naver?query={idol}')

