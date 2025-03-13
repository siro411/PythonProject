x=True
print(x)
print(type(x))
print(x+10) #11 --> 1+10
print(False+10)  #10 --> 0+10
print('------------')
print(bool(18))
print(bool(0),bool(0.0))
#总结非0的bool值都为True
print(bool('hello'))
print(bool(''))
#所有非空字符串的布尔值都是True
print(bool(False)) #False
print(bool(None))  #False