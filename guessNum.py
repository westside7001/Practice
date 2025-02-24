import random,os
from logging import exception

r = random.randint(1, 50)
print(r)
print('請猜個數字，從 1 ~50')
value = input('選一個數字吧,只有五次機會哦\n')

def checkNum(value):
    if isinstance(value, int):
        return value
    try:
        return int(value)  # 嘗試將字串轉換為數字
    except Exception as e:
        print('錯誤，請輸入整數')
        os._exit(1)

value = checkNum(value)
i=1
t=4
while i <= t :
    if r == value:
        print('恭禧猜中')
        break
    elif r < value:
        print('請猜小一點的數字，剩',t - i,'次')
        i +=1
        value = int(input())
    elif r > value:
        print('請猜大一點的數字，剩',t - i,'次')
        i += 1
        value = int(input())

print('五次都沒中，請重新猜一次')

