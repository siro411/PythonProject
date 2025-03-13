def get_sum(num): #num叫形式参数
    s=0
    for i in range(1,num+1):
        s+=i
    return s

print(get_sum(num=10)) #10是实际参数值