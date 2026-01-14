(=====if 제어문 예시=====)
money = True

if money:
  print("택시를 타고 가라"")
else:
  print("걸어가라")
>>> 택시를 타고 가라

(=====비교연산자 예시=====)
money = 2000

if money >= 3000:
  print("택시를 타고 가라")
else:
  print("걸어가라")
>>> 걸어가라

(=====and, or, not 예시=====)
money = 2000
card = True

if money >= 3000 or card:
  print("택시를 타고 가라")
else:
  print("걸어가라")
>>> 택시를 타고 가라

(=====in, not in 예시=====)
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
  print("택시를 타고 가라")
else:
  print("걸어가라")
>>> 택시를 타고 가라

(=====elif 예시=====)
pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
  print("택시를 타고 가라")
elif card:
  print("택시를 타고 가라")
else:
  print("걸어가라")
>>> 택시를 타고 가라


(=====while 반복문 예시=====)
treeHit = 0
while treeHit < 10:
  treeHit +=1
  print(f"나무를 {treeHit}번 찍었습니다")
  if treeHit == 10:
    print("나무 넘어갑니다")

(=====중첩 while문 예시=====)
i = 1
while i <= 3:
	j = 1
	while j <= 3:
		print(f"i={i}, j={j}")
		j += 1
	i += 1

>>> i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3


(=====for 반복문 예시=====)
list = ['one', 'two', 'three']
for i in list:
  print(i)
>>> one
two
three

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
  print(first + last)
>>> 3
7
11

(=====range() 예시=====)
add = 0
for i in range(1, 11):
  add += i
print(add)
>>> 55

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):           # range(len(marks)) == range(5)
  if marks[number] < 60:
    continue
  print(f"{number + 1}번 학생 축하합니다, 합격입니다.")



