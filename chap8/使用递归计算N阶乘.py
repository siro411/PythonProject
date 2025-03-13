def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))

def fac2(n):
    if n==1 or n==2:
        return 1
    else:
        return fac2(n-1)+fac2(n-2)

print(fac2(9))

for i in range(1,10):
    print(fac2(i),end='\t')