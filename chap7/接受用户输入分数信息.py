try:
    score=int(input('请输入分数：'))
    if 100>=score>=0:
        print('分数为：',score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)

