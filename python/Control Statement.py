(=====if문 예시=====)
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
