import re
pattern='\d\.\d+'
s='I study Python 3.11 every day'
match=re.match(pattern,s,re.I) #忽略大小写
print(match) #None
s2='3.11Python I study ever day'
match2=re.match(pattern,s2) #忽略大小写
print(match2) # <re.Match object; span=(0, 4), match='3.11'>

print('匹配值的起始位置：',match2.start())
print('匹配值的结果位置：',match2.end())
print('匹配区间的位置',match2.span())
print('待匹配的字符串',match2.string)
print('匹配的数据',match2.group())