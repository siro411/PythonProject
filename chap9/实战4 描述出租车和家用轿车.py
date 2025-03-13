class Car:
    def __init__(self,model,no):
        self.model=model
        self.no=no

    def start(self):
        pass
    def stop(self):
        pass

class Taxi(Car):
    def __init__(self,model,no,company):
        super().__init__(model,no)
        self.company=company

    def start(self):
        print('出租车在启动')

    def stop(self):
        print('出租车在停止')

class Mycar(Car):
    def __init__(self,model,no,owner):
        super().__init__(model,no)
        self.owner=owner

    def start(self):
        print('我的车在启动')

    def stop(self):
        print('我的车在停止')

taxi=Taxi('大众','京A8888','长城出租车公司')
taxi.start()
taxi.stop()