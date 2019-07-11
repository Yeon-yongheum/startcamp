"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}


# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
# sum 함수
print(sum(score.values())/len(score))
# 일반적
result = 0
count = 0
for score_value in score.values():
    result += score_value
    count += 1
print (result/len(score))




# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
# total_score = 0 
# person_sum = 0
# person_avg = 0
# total_avg = 0
# for name, person_scores in scores.items():
    
#     for score in person_scores.values():
#         person_sum += score
#     person_avg = person_sum/len(person_scores)    
#     print (f'{(name)} 평균은 {person_avg}')
#     total_score += person_avg
#     person_sum = 0
# total_avg = total_score/len(scores)
# print(f'전체 평균은 {total_avg}')

for name in scores.keys():
    sum = 0
    total = 0
    for score in scores[name].values():
        sum += score
        avg = sum/len(scores[name])
    print(f'{name} {avg}')
    total += avg
print(f'{total/len(name)}')









# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?


# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name,temp in city.items():
    print(name, temp)
    avg = sum(temp)/len(temp)
    print(f'{name} : {avg:.2f}') # f-string : 3.6+
    print('{} : {:.2f}'.format(name,avg)) # format-string
    print(name,' : ', avg)





# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
# 모든 지역의 온도를 모두 확인하면서,
for name, temp in city.items():
    if count == 0 :
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 떄도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
for temp in city['서울']:
    if temp == 2:
        print('네')
    else:
        print('아니요')

if 2 in city ['서울']:
    print('네')
else:
    print('아니요')