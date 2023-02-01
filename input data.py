
#Multiple assignment in python

num1 = num2 = num3 = 0     
print(num1, num2, num3)

#Multi-value assignment in python

name, page_count, price = "Python", 300, 254.65

print(name, page_count, price)

#Converting integer to float
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print("Value:",new_number)
print("Data type:",type(new_number))

#Addition of integer and string using explicit conversion

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

#Example of and, or, not, True, False keywords
print("example of True, False, and, or not keywords")
 
#  compare two operands using and operator
print(True and True)
 
# compare two operands using or operator
print(True or False)
 
# use of not operator
print(not False)

#Example of a break, continue
# execute for loop
for i in range(1, 11):
     
    # print the value of i
    print(i)
     
    # check the value of i is less than 5
    # if i lessthan 5 then continue loop
    if i < 5: 
        continue
         
    # if i greater than 5 then break loop
    else: 
        break

#Example of def, if, and else keywords
def GFG():
    i=20
    # check i is odd or not
    # using if and else keyword
    if(i % 2 == 0):
        print("given number is even")
    else:
        print("given number is odd")
GFG()    









