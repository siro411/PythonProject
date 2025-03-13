lst=[
    ['01','电风扇','美的',500],
    ['02', '洗衣机', 'TCL', 1000],
    ['03', '微波炉', '老板', 400]
]
print('编号\t\t名称\t\t品牌\t\t单价')
for items in lst:
    for i in items:
        print(i,end='\t\t')
    print()

for items in lst:
    items[0]='0000'+items[0]
    items[3]='{0:.2f}'.format(items[3])

print('编号\t\t名称\t\t品牌\t\t单价')
for items in lst:
    for i in items:
        print(i,end='\t\t')
    print()