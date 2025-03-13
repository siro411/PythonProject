lst=['hello','world','python']
print('原列表',lst,id(lst))
lst.append('anna')
print('增加元素之后，',lst,id(lst))

lst.insert(1,100)
print(lst)
lst.remove('world')
print('删除元素之后的列表',lst,id(lst))

#使用pop(index)根据索引将元素去除，然后再删除
print(lst.pop(1))
print(lst)
# lst.clear()
# print(lst,id(lst))
lst.reverse()
print(lst)
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

lst[1]='mysql'
print(lst)