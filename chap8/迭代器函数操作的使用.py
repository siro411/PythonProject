lst=[54,56,77,4,567,34]
#排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表：',lst)
print('升序：',asc_lst)
print('降序：',desc_lst)

#reversed反向
new_lst=reversed(lst)
print(type(new_lst)) #<class 'list_reverseiterator'>
print(list(new_lst))

#zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))
# print(dict(zipobj))

# enumerate
e=enumerate(y,start=1)
print(type(e)) #<class 'enumerate'>
print(tuple(e))

#all
lst2=[10,20,'',30]
print(all(lst2)) #False 有空字符串
print(all(lst)) #True

#any
print(any(lst2)) #True 列表中有一个为True就为True了，所有都是False，输出才是False

#next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))

#filter
def fun(num):
    return num%2==1

obj=filter(fun,range(10)) # 将0-9的整数
print(list(obj)) # [1, 3, 5, 7, 9]

def upper(x):
    return x.upper()
new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2)) #['HELLO', 'WORLD', 'PYTHON']
