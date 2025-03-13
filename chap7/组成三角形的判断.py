try:
    a = int(input('请输入第一条边'))
    b = int(input('请输入第二条边'))
    c = int(input('请输入第三条边'))
    if a+b>c and a+c>b and b+c>a:
        print(f'三角形的边长为a={a},b={b},c={c}')
    else:
        raise Exception(f'a={a},b={b},c={c},不能构成三角形')
except Exception as e:
    print(e)