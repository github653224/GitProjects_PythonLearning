class Animal():
    def run(self):
        print('animal is running')

a=Animal()
a.run()

class Dog(Animal):
    pass
b=Dog()
b.run()

class Cat(Animal):
    def run(self):
        print('cat is running')
c=Cat()
c.run()



