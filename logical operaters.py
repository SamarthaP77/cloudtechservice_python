#Logical Operator
L = 90
M = 20
if(L>10 and M<10):
    print("Yes")
else:
    print("No")

#Membership Operator
List = [10,20,78,98,60]
print(20 in List)
print(78 not in List)


#Identity Operator
a = 3
print(a is 3)
print(a is not 3)

#Decision Making
#if statement
b = 67
if b>56:
    print("b is true")

#if....else statement
a = 90
b = 788
if a<b:
    print("a is greater")
else:
    print("b is greater")

    
a = 789
if a%3==0:
    print("a is an odd number")
else:
    print("a is an even number")

#Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print"Bye".

num = int(input("Enter the number"))
if num%5==0:
    print("Hello")
else:
    print("Bye")
    
#Write a program to check whether the last digit of a number(entered by user)is divisible by 3 or not.
num = int(input("Enter the number: "))
id = num%10
if id%3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#Nested if statement

b = 90
if b>80:
    if b>100:
        print("It is true")
    else:
        print("It is also true")
else:
    print("It is not true")
    
