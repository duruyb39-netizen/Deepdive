# 올바른 변수명 예시
name = "홍길동"
age = 25
user_name = "gildong"
userName = "gildong"       # 카멜 케이스
_private = "비공개"
count1 = 10

# 잘못된 변수명 예시
1name = "홍길동"            # 숫자로 시작(오류)
user-name = "홍길동         # 하이픈 사용(오류)
if = 10                   # 예약어 사용(오류)

# 리스트 복사
a = [1, 2, 3]
b = a

print(id(a))
>>> 4303029896

print(id(b))
>>> 4303029896            # id(a) == id(b)

# [:] 이용하기
a = [1, 2, 3]
b = a[:]
a[1] = 4

print(a)
>>> [1, 4, 3]

print(b)
>>> [1, 2, 3]            # a 리스트의 값을 바꿔도 b 리스트는 바뀌지 않음

from copy import copy
a = [1, 2, 3]
b = copy(a)              # b = copy(a) == b = a[:]
