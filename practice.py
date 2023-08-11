import random
import re
import camelcase
A,B=float(3),float(5)

ADD=A+B
#Casting
print(float(ADD))

X='BEST'

def func():
    X='GOOD'
    print('Pyhton is '+X)
func()

print(random.randrange(1,15))


# Strings
print(X[1:3])
print(X.lower())
print(X.replace("B","T"))

#format String
age=22
height=6
ME="My age is {} and my height is {}"
print(ME.format(age,height))

print("The \"peaky blinder\" series is top notch")
print(X.encode())

# Python list

A=['ALI','AHMED','MARYAM','ASMA',50,True]
print(A)
print(A[2])
print(A[3:5])
print(A[-5:-1])

if "AL" in A:
 print(True)
else:
   print(False)

#change list items

A[1:3]=['REHAN','ZAIN']
print(A)

# ADD ITEM

A.insert(1,"AAMRAH")
print(A)

#LOOPS

for x in A:
   print(x)

for x in range(len(A)):
   print(A[x])

#sorting list
thisList=['B','Z','A']
thisList.sort()
print(thisList)

#joining two lists

for x in thisList:
   A.append(x)

print(A)

#tuple

aTuple=('A','Z','B')
print(aTuple)

print(aTuple[1])

# updating tuple

bTuple=list(aTuple)
bTuple[1]=('C')
aTuple=tuple(bTuple)
print(aTuple)

#sets

S1={'A','B','C'}
S2={'S','A','K'}
S3=S1.intersection(S2)
print(S3)

#dictionaries

thisdict=dict(car='honda',
         model='2023' )
print(thisdict)
x=thisdict.get('model')
print(x)
y=thisdict.keys()
print(y)

def function(fName,lName):
   print(""+fName+ " "+lName)

function("azan","noor")

#lambda function

x=lambda a:a+10
print(x(5))

#keyword arguments

def myfunc(**kid):
  print("kid last name is: "+kid['lName'])

myfunc(fName='azan',lName='noor')

#iterator

itr="pakistan"
for x in itr:
   print(x)

#RegEX
text='my name is ahmed'
r=re.search("^m.*ahmed$",text)
if r:
   print("yes")
else:
   print("no")

#updated PIP and downloaded a package

text="my name is rahyma"
c=camelcase.CamelCase()
print(c.hump(text))

#String formatting

Myage=22
new="my age is {}"
print(new.format(Myage))

