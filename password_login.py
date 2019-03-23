password = 'a123456'
i = 0
while True:
    inputpass = input('请输入密码(最多输入三次)：')
    if inputpass == password:
        print('登陆成功')
        break
    else:
        i = i + 1
        if i >= 3:
            print('三次错误，登陆失败')
            break
        print('密码错误！还有', 3-i, '次机会')
    
