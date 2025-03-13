for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print() #空语句，作用是换行

print('-------------直角三角形')
for i in range(1, 6):
    print(i*'*', end='')
    print()  # 空语句，作用是换行

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print() #空语句，作用是换行

print('-------------倒三角形')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print() #空语句，作用是换行

print('-------------等腰三角形')
for i in range(1,6):
    for j in range(1,6-i):
            print(' ', end='')
    for k in range(1,2*i):
            print('*', end='')
    print() #空语句，作用是换行