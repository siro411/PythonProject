#存储和读取一维数据
def my_write():
    lst=['ann','bebe','cc','dd']
    with open('student.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))

def my_read():
    with open('student.csv','r') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)

#存储和读取二维数据
def my_write_table():
    lst=[
        ['商品名称','单价','采购数量'],
        ['水杯','98.5','20'],
        ['鼠标','89','100']
    ]
    with open('products.csv','w',encoding='utf-8') as file:
        for item in lst:
            line=','.join(item)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]
    with open('products.csv','r',encoding='utf-8') as file:
        lst=file.readlines()
        for item in lst:
            new_lst=item[:len(item)-1].split(',')
            data.append(new_lst)
    print(data)

if __name__=='__main__':
    # my_write()
    # my_read()
    my_write_table()
    my_read_table()