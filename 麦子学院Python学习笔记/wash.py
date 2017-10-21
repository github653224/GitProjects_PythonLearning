class  Washer:      #非智能洗衣机
    def __init__(self):
        self.water=0
        self.scour=0
    def add_water(self,water):
        print('add water:',water)
        self.water=water

    def add_scour(self,scour):
        self.scour=scour
        print('add scour:',self.scour)

    def start_wash(self):
        print('start washing ....')

if __name__=='__main__':
    w=Washer()
    w.add_water(10)
    w.add_scour(2)
    w.start_wash()
