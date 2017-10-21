class  Washer:              #比较智能+半人工的自动化洗衣机
    def __init__(self,water=10,scour=2):
        self._water=water  #属性私有化
        self.scour=scour

    @property        #属性的包装
    def water(self):
        return self._water

    @water.setter
    def water(self,water):
        if 0<water<=500:
            self._water=water
        else:
            print('set Failure')




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
    print(w.water)
    w.water=1000
    print(w.water)



