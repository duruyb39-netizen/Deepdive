def add(a, b):
  return a + b
# 이 함수의 이름은 add, 입력으로 2개의 값을 받으며 반환값(출력값)은 2개의 입력값을 더한 값이다.

a = 3
b = 4
c = add(a, b)    # add(a, b)의 반환값을 c에 대입
print(c)
>>> 7

(====일반적인 함수 예시====)
def add(a, b): 
    result = a + b 
    return result

(====입력값의 개수가 미정일 때====)
def add_many(*args):    # *args는 “가변 인수(variable-length arguments)”를 의미
  result = 0
  for i in args:
    result += i
  return result
result = add_many(1, 2, 3)
print(result)
>>> 6

>>> def add_mul(choice, *args): 
     if choice == "add":            # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul":          # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
     return result 

result = add_mul('add', 1,2,3,4,5)
print(result)
>>> 15

(====키워드 매개변수, kwargs====)
def create_profile(**info):
  print("===프로필 정보===")
  for key, value in info.items():
    print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업='프로그래머', 취미='독서')
>>> ===프로필 정보===
이름: 김철수
나이: 30
직업: 프로그래머
취미: 독서

(====lambda 예약어====)
add = lambda a, b: a+b
result = add(3, 4)
print(result)
>>> 7
