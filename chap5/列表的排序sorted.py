lst=[4,56,3,40,89,56]
print('原列表',lst)
asc_lst=sorted(lst)
print('升序',asc_lst)
print('原列表',lst)

desc_lst=sorted(lst,reverse=True)
print('降序',desc_lst)
print('原列表',lst)

#忽略大小写进行排序
lst2=['banana','apple','Cat','Orange']
print('原列表',lst2)
new_lst2=sorted(lst2,key=str.lower)
print('原列表',lst2)
print('排序后的列表',new_lst2)
