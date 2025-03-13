def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('2020年东京奥运会')

def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
        print(file.read)

def copy(src,target):
    with open(src,'r',encoding='utf-8') as file:
        with open(target,'w',encoding='utf-8') as file2:
            file2.write(file.read())

if __name__ == '__main__':
    write_fun()
    read_fun()
    copy('./aa.txt','./dd.txt')
