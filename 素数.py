from math import sqrt
num = int(input('请输入正整数：'))
flag = True
num1 = int(sqrt(num))
for x in range(2, num1+1):
    if num % x == 0:
        flag = False
        break
if flag == False or num == 1:
    print('%d is not sushu' % num)
else:
    print('%d is sushu' % num)
