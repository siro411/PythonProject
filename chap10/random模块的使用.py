import  random
random.seed(10)
print(random.random()) #[0.0,1.0)
print(random.random())

print('-'*30)
random.seed(10)
print(random.randint(1,100)) #[1,100]

for i in range(5): #[m,n)步长为k
    print(random.randrange(1,10,3))

print(random.uniform(1,100)) #[a,b]随机小数

lst=[i for i in range(1,11)]
print(lst)
print(random.choice(lst)) #lst是列表，称为序列

random.shuffle(lst)
print(lst)


