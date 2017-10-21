class Student():
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

a=Student('panxueyan',100)
a.print_score()
print(a.get_name())
print(a.get_score())
a.set_score(98)
print(a.get_score())