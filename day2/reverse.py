with open('number.txt', 'w') as file:
    for i in range(6):
        file.writelines(f'{i}\n')
#number.txt를 읽어서
# 리스트 (readlines)
with open('number.txt', 'r') as file:
    numbers = file.readlines()
print(numbers)

#리스트를 뒤집는다.
numbers.reverse()

with open('number_revers.txt', 'w') as file:
    for number in numbers:
        file.write(number)
# number_reverse.txt로 저장