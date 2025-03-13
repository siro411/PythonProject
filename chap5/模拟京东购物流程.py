# cat=input('请输入商品编号和名称：')
lst=[input('请输入商品编号和名称：') for i in range(5)]
for i in lst:
    print(i)

cart=[]
while True:
    flag=False
    num=input('请输入商品编号')
    if num.lower() == 'q':
        break
    # for products in lst:
    #     if num in products:
    #         cart.append(products)
    #         print('该商品已经成功添加到购物车')
    #         break
    # else:
    #     print('该商品不存在')
    for product in lst:
        if num==product[0:4]:
            flag = True
            cart.append(product)
            print('该商品已经成功添加到购物车')
            break
    if not flag:
        print('该商品不存在')


cart.reverse()
for i in cart:
    print(i)
