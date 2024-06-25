from add import add_func #Master가 add.py 파일에 add_func(n1, n2) / 정수 반환 함수 작성
from sub import sub_func #Foo가 sub.py 파일에 sub_func(n1, n2) / 정수 반환 함수 작성

## 전역 변수부
num1, num2, res = 100, 200, 0

## 메인 코드부
res = add_func(num1, num2)
print('더한 결과 :', res)

res = sub_func(num1, num2)
print('뺀 결과 :', res)