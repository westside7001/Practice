

password = 'a123456'
i = int(3)
while 0 <= i <=3:
    pwd = input('請輸入密碼\n')
    if pwd == password:
        print('密碼正確，登入成功')
        break
    else:
        i = i-1
        print('密碼錯誤，還有',i,'次機會')
        if i == 0:
            print('嚐試次數過多')
            break
