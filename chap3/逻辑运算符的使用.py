print(True and True)
print(True and False)
print(False and False)
print(False and True)

print('-'*40)
print(8>7 and 6>5) #True
print(8>7 and 6<5) #False
print(8<7 and 10/0)  #False,当第一个表达式为False时，直接得结果，不会计算and右边的表达式了

print('-'*40)

print(True or True)
print(True or False)
print(False or False)
print(False or True)
print(8>7 or 10/0) #True 当左侧为True or右侧不执行

print(not True)
print (not False)
print(not (8>7))  #False