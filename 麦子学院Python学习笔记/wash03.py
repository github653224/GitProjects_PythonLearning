class  Washer:              #比较智能+半人工的自动化洗衣机
    def __init__(self,water=10,scour=2):
        self.water=water
        self.scour=scour

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
    w.start_wash()

    wb=Washer(100,10)
    wb.set_water(50)
    wb.set_scour(6)
    wb.start_wash()
# add water: 10
# add scour: 2
# start washing ....
# add water: 50
# add scour: 6
# start washing ....