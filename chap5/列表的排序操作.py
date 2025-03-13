lst=[4,56,3,40,89,56]
lst.sort()
print('升序：',lst) #排序是在原列表的基础上进行的

lst.sort(reverse=True)
print('降序：',lst)

print('-----------')
lst2=['banana','apple','Cat','Orange']
print('原列表',lst2)
lst2.sort()
print('升序',lst2)
lst2.sort(reverse=True)
print('降序',lst2)

lst2.sort(key=str.lower)
print(lst2)