def get_sum(s):

    ss=0;
    for i in s:
        if i.isdigit():
            ss+=eval(i)
    return ss
s=input('请输入一个字符串：')
print(get_sum(s))

