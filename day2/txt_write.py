# option 1
# # 파일을 연다.
# open(파일명, 옵션)
# w : write (덮어쓰기)
# a : append (이어쓰기)
f = open('ssafy.txt', 'w')
# 글을 작성한다.
for i in range(10):
    # \n : 개행문자 (엔터 : newline)
    f.write(f'hello! {i}\n')

# 파일을 닫는다.
f.close()

# option 2커택스트 매니저 (context manager) with 구문
with open('ssafy_with.txt', 'w') as f:
    for i in range(1):
        f.writelines('안녕?\n222\n33\n')
        f.writelines(['a\n','b\n'])