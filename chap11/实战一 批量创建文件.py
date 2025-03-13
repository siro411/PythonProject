import os
import random

def create_file(path):
    with open(path,'w',encoding='utf-8') as file:
        pass

if __name__=='__main__':
    dir='./data'
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir('./data')
    lst = ['水果', '烟酒', '粮油', '肉蛋', '蔬菜']

    for i in range(1, 3001):
        s = random.choice(lst)
        hex_number = f"{random.randint(0, 0xFFFFFFFFF):09X}"
        idx = '0' * (4 - len(str(i))) + str(i)
        path = os.getcwd() + '/' + idx + '_' + s + '_' + hex_number + '.txt'
        create_file(path)