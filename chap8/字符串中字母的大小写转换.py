def switch(s):
    new_s=''
    for i in s:
        if i.isupper():
            new_s+=i.lower()
        elif i.islower():
            new_s+=i.upper()
        else:
            new_s+=i
    return new_s
print(switch('HELLO123world'))