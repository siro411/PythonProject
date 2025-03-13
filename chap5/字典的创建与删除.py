d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) #当key相同时，value值进行了覆盖

lst1=[10,20,30]
lst2=['cat','dog','pet']
zipobj=zip(lst1,lst2)
print(zipobj) #zip对象
#print(list(zipobj)) #[(10, 'cat'), (20, 'dog'), (30, 'pet')]
d=dict(zipobj)
print(d)

#使用参数创建字典
d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10}) #t是key，10是value，元组是可以作为字典中的key

# l=[10,20,30]
# print({l:10}) #TypeError: unhashable type: 'list'

#字典属于序列
print(max(d))
print(min(d))
print(len(d))

del d
# print(d)