import platform
import myModule

#classes
class myClass:
    speed=50
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
       print("my name is "+self.name)

p1=myClass('azan',20)
p1.myfunc()

#inheritance 
class child(myClass):
    pass

p2=child('zainab',18)
print(p2.age)

#polymorphism

class Car:
    def __init__(self,brand,model) :
        self.brand=brand
        self.model=model
    def myfunc(self):
        print("race")
class plane:
    def __init__(self,brand,model) :
        self.brand=brand
        self.model=model
    def myfunc(self):
        print("fly")
class boat:
    def __init__(self,brand,model) :
        self.brand=brand
        self.model=model
    def myfunc(self):
        print("sail")
p1=Car("honda","2020")
p2=plane("PIA","2023")
p3=boat("titanic","1900")

for x in(p1,p2,p3):
    x.myfunc()

x=platform.system()
print(x)

def greet(name):
    print("hello "+name)

greet("esha")

myModule.greet1()
