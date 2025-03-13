answer=input('请问您喝酒了嘛')
if answer=='y':
    proof=eval(input('请输入酒精含量'))
    if proof<20:
        print('不构成酒驾，祝您一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车')
    else:
        print('已构成醉驾，千万不要开车')
else:
    print('请继续开车')