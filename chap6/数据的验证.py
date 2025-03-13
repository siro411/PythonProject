print('123'.isdigit()) #True
print('一二三'.isdigit()) #False
print('III'.isdigit()) #False

#所有字符都是数字
print('123'.isnumeric()) #True
print('一二三'.isnumeric()) #True
print('X'.isnumeric()) #False
print('壹贰叁'.isnumeric()) #True
print('-'*40)

#所有字符都是字母
print('hello你好'.isalpha()) #True
print('hello你好123'.isalpha()) #False
print('hello你好一二三'.isalpha()) #True
print('-'*40)

#所有字符都是数字或者字母
print('hello你好'.isalnum()) #True
print('hello你好123'.isalnum()) #True
print('hello你好一二三'.isalnum()) #True

print('-'*40)
#判断字母的大小写
print('HelloWorld'.islower()) #False
print('helloworld'.islower()) #True
print('hello你好'.islower()) #True
print('-'*40)

#判断字母的大小写
print('HelloWorld'.isupper()) #False
print('HELLOWORLD'.isupper()) #True
print('HELLO你好'.isupper()) #True
print('-'*40)

#所有字符都是首字符大写
print('Hello'.istitle()) #True
print('HelloWorld'.istitle()) #False W不是首字母但是大写了
print('Helloworld'.istitle()) #True
print('Hello world'.istitle()) #False
print('-'*40)

#判断是否都是空字符
print('\t'.isspace()) #True
print(' '.isspace()) #True
print('\n'.isspace()) #True
