# import random
# import pprint
# import requests
# url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
# # 1. 요청
# # 2. json -> 
# # 파이썬의 dictionary로 변환하여 조작할 수 있다.
# # 응답 (HTML, XML, JSON)
# response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response))
# # number = [response['drwtNo1'],response['drwtNo2'],response['drwtNo3'],response['drwtNo4'],response['drwtNo5'],response['drwtNo6']]
# number = []
# for i in range(1,7):
#     number.append(response[f'drwtNo{i}'])
# bonus = response['bnusNo']
# print(number)
# print(bonus)
# win = [0,0,0,0,0,0]
# # one = 0
# # two = 0
# # three = 0
# # four = 0
# # five = 0
# # six = 0
# bonuspoint = 0
# # for cnt in range(500000):
# #     count = 0
# #     # my_lotto = random.sample(range(1, 46), 6)
# #     # print(my_lotto)
# #     for i in my_lotto:
# #         if bonus == i:
# #             bonuspoint += 1
# #         for result in number:
# #             if result == i:
# #                 count += 1
# #     if count == 6 :
# #         # print('1등')
# #         one += 1
# #     elif count == 5 and bonuspoint == 1:
# #         # print('2등')
# #         two += 1
# #     elif count == 5 :
# #         # print('3등')
# #         three += 1
# #     elif count == 4 :
# #         # print('4등')
# #         four += 1
# #     elif count == 3 :
# #         # print('5등')
# #         five += 1
# #     elif count == 2 :
# #         # print('6등')
# #         six += 1
# #     # else:
# #     #     # print('꽝')
# #     bonuspoint = 0
# for i in range(10000000):
#     my_lotto = random.sample(range(1, 46), 6)

#     matched = len(set(number) & set(my_lotto))  
#     if matched == 6:
#         win[0] += 1
#     elif matched == 5 and bonus in my_lotto:
#         win[1] += 1
#     elif matched == 5:
#         win[2] += 1
#     elif matched == 4:
#         win[3] += 1
#     elif matched == 3:
#         win[4] += 1
#     elif matched == 2:
#         win[5] += 1


#     print(win, end='\r')

    
# # print(one)
# # print(two)
# # print(three)
# # print(four)
# # print(five)
# # print(six)
    
#선생님꺼

import random
import pprint
import requests
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
# 1. 요청
# json -> 
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response))

# 당첨번호 6개 + 보너스 번호
win_lotto = []
bonus = response['bnusNo']
for i in range(1, 7):
    win_lotto.append(response[f'drwtNo{i}'])

result = [0, 0, 0, 0, 0]
for i in range(10000000):
    # 내가 뽑은 로또 번호
    my_lotto = random.sample(range(1, 46), 6)

    # 몇개 맞았는지 확인
    # matched = 0
    # for num in my_lotto:
    #     if num in win_lotto:
    #         matched += 1
    matched = len(set(win_lotto) & set(my_lotto))

    # 몇개 맞았는지를 바탕으로 출력
    if matched == 6:
        result[0] += 1
    elif matched == 5 and bonus in my_lotto:
        result[1] += 1
    elif matched == 5:
        result[2] += 1
    elif matched == 4:
        result[3] += 1
    elif matched == 3:
        result[4] += 1
    print(result, end='\r')
print('끝')
print(result)

