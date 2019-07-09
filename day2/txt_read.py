#window - cp949 
# mac/web - utf-8
with open('ssafy_with.txt', 'r') as f:
    #readlines : 라인을 각각 리스트의 원소로 하여 반환한다.
    lines = f.readlines()
    print(lines)
    print(f.readlines())
    print(type(f.readlines()))

for line in lines:
    print(line.strip())
    # print(line)

with open ('ssafy.txt', 'r') as f:
    #read : 전체 내용을 하나의 string으로 반환한다
    txt = f.read()

print(txt)