import re

chepai=['京A8888','津B66666','吉A77766']
for i in chepai:
    print(i,'归属于地',i[0])

s='HelloPython,HelloJava,hellophp'
# pattern=input('请输入要统计的字符：')
# cnt_list=re.findall(pattern,s,re.I)
# print('{0}在{1}中一共出现了{2}次'.format(pattern,s,len(cnt_list)))

word=input('请输入要统计的字符：')
print('{0}在{1}中一共出现了{2}次'.format(word,s,s.upper().count(word.upper())))

