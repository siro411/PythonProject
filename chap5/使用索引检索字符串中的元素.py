s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print('\n----------------')

for i in range(-10,0):
    print(i,s[i],end='\t')

print()
print(s[0:5:2])
print(s[:5:1])
print(s[:5:])
print(s[0::1]) #默认到序列的最后一个位置

print(s[5::])
print(s[5:]) #两个代码功能相同，省略了结束，省略了步长

print(s[::2]) #0,2,4,6,8
print(s[::-1]) #逆序
