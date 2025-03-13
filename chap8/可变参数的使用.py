def fun(*para):
    print(type(para))
    for item in para:
        print(item)

fun(10,20,30,40)
fun(10)
fun(30,40)
fun([11,22,33,44]) #一个列表放到了元组中

#在调用时，参数前加一颗星，将列表进行解包
fun(*[11,22,33,44])

def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'-->',value)

fun2(name='jxj',age=18)

d={'name':'jzj','age':18} #TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)