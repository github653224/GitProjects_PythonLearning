class  Washer:              #比较智能的自动化洗衣机
    def __init__(self):
        self.water=0
        self.scour=0

    def set_water(self,water):
        self.water=water

    def set_scour(self,scour):
        self.scour=scour

    def add_water(self):
        print('add water:',self.water)


    def add_scour(self):

        print('add scour:',self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()
        print('start washing ....')

if __name__=='__main__':
    w=Washer()
    w.set_water(10)
    w.set_scour(2)
    w.start_wash()
