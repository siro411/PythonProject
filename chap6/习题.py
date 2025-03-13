import re

word='三更灯火五更鸡，正是男儿读书时'
print(word.index('正是男儿读书时'))
print(word.find('黑发不知勤学早')) #-1
#print(word.index('白首方悔读书迟'))  #ValueError: substring not found

s1='中国梦'
lst=['伟大','美丽']
s3=s1.join(lst)
print(s3)

pattern=r'\s*@'
s='@ysj @lmm @gxc'
lst=re.split(pattern,s)
print(lst)