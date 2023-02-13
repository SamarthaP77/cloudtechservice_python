#Dictionary methods
#Copy method.
a = {'Place':'kathmandu','Time':3,'location':'budhanilkantha'}
b = a.copy()
print(b)

#Usage of fromkeys() method.
ok = {'name','age','sex'}
dict = dict.fromkeys(ok)
print(dict)
dict = dict.fromkeys(ok,10)
print(dict)

#Use of get method
print(a.get('Time'))
print(a['Time'])

#Item method
print(a.items())

#Prints all the keys in the dictionary
print(a.keys())

#Prints all the values in the dictionary
print(a.values())

#Set default value()
print(a.setdefault('Place',None))

#Update method
a = {'Place':'kathmandu','Time':3,'location':'budhanilkantha'}
b = {'Gender':'Male', 'Name':'Samartha','Level':'Bachelors'}
a.update(b)
print(a)
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)


#Functions
def samartha(a,b):
    addition = a + b
    print(addition)
samartha(5,3)
#Substraction of any two numbers
def sub(x,y):
    s = x - y
    return s
x=int(input("Enter your first number: "))
y=int(input("Enter your second number:"))
print(sub(x,y))

#Multiplication of two numbers
def mul(p,q,r):
    a = p*q*r
    print (a)
p=int(input("Enter your first number: "))    
q=int(input("Enter your second number: "))    
r=int(input("Enter your third number: "))
mul(p,q,r)

#Function without argument and without return type
def samartha():
    print("Hello Nepal")
samartha()

#Anonymous Function
#To find sum of two uesers using lambda function 
sum=lambda a,b: a+b
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print(sum(a,b))

#Multiplication of two numbers using lambda function
mul=lambda a,b,c: a*b*1
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))
print(mul(a,b,c))

#Recursive Function
#To find the factorial of a given number
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print("The factorial is: ",end=" ")    
print(fact(7))
     
