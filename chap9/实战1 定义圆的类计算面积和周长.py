class Circle():
    def __init__(self,r):
        self.r=r

    def get_area(self):
        return 3.14*pow(self.r,2)

    def get_perimeter(self):
        return 2*3.14*self.r

r=eval(input('请输入圆的半径'))
c=Circle(r)
print('圆的面积为：',c.get_area())
print('圆的周长为：',c.get_perimeter())




