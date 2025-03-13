import random

def maxis(lst):
    s=lst[0]
    for i in lst:
        if(i>s):
            s=i
    return s

print(maxis([40,76,28,25,42,17,56,53,43,20]))
