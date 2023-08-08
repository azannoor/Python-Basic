class myClass:
    speed=50
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
       print("my name is "+self.name)

p1=myClass('azan',20)
p1.myfunc()

class child(myClass):
    pass

p2=child('zainab',18)
print(p2.age)