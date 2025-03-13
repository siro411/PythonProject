s1='HelloWorld'
new_s2=s1.lower() # helloworld
print(s1,new_s2)

new_s3=s1.upper()
print(s1,new_s3)

e_mail='ysj@126.com'
lst=e_mail.split('@')
print('邮箱名:',lst[0],'服务器域名:',lst[1])

print(s1.count('o')) #2
print(s1.find('o'))
print(s1.find('v')) #-1 没有找到

print(s1.index('o'))
# print(s1.index('v')) ValueError: substring not found

print(s1.startswith('H')) #True
print(s1.startswith('P')) #False

print('demo.py'.endswith('.py')) #True
print('text.txt'.endswith('.txt')) #True
