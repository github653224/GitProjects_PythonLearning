class Student :
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def instructe(self):
        print('hi i am '+self.name)
        print('{}\'s grade is {}'.format(self.name,self.grade))
    def improve(self,amount):
        self.grade+=amount

jj=Student('xiaoming',59)
jj.instructe()

jj.improve(1)
jj.instructe()

# hi i am xiaoming
# xiaoming's grade is 59
# hi i am xiaoming
# xiaoming's grade is 60