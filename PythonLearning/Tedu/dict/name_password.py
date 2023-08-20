while True:
    name = input('请输入用户名：')
    password = input('请输入密 码：')
    # 验证两次密码是否一致
    password_again = input('请确认密 码：')

    if password != password_again:
        print('两次输入的密码不一致，请重新输入')
        continue

    # 验证用户名和密码是否有空格
    if ' ' in name or ' ' in password:
        print('用户名和密码不能有空格，请重新输入')
        continue

    print('用户名和密码创建成功！')
