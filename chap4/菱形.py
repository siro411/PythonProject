row=eval(input('请输入菱形的行数'))
while row%2==0:
    print('请重新输入菱形的行数')
    row = eval(input('请输入菱形的行数'))

top_row=(row+1)//2
for i in range(1, top_row+1):
    for j in range(1, top_row +1- i):
        print(' ', end='')
    for k in range(1, 2 * i):
        print('*', end='')
    print()  # 空语句，作用是换行

bottom_row=row//2
for i in range(1, bottom_row+1):
    #直角三角形
    for j in range(1, i+1):
        print(' ', end='')
    #倒三角形
    for k in range(1,2*(bottom_row +1-i)):
        print('*', end='')
    print()  # 空语句，作用是换行
