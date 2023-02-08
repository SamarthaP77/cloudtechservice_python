#Updating Lists
z = [88,90,67,67,90]
#Update the item at index with the string "Samartha"
z[1] = "Samartha"
print(z)
#Appending or adding a new value to a list
z.append('football')
print(z)

#Deleting list elements
#Using del statement
a = ["Python",100,"football",2,"is"]
del a[0]
print(a)


#Basic List Operators
a = [7,8,9,0,6]
b = [9,8,6,5,6]
print(a + b)
print(a*4)
print(6 in b)
print(9 not in a)
print(len(a))
print(max(b))
print(min(a))

#Built-in List Functions and Methods

d = [10,15,20,'Hello','Python',10]
d.append('Hello')
print(d)
print(d.count(10))
e = [900,800]
d.extend(e)
print(d)
print(d.index('Hello'))
d.insert(2,"ok")
print(d)
print(d.pop())
print(d.pop(3))
print(d)
d.reverse()
print(d)


#Write a python program to sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


#Replace list value with a new item if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#Tuples
T = (99,18,'Hi',12,"Hello",15.55,'Pragramming',100,125.5)
print(T[5])
print(T[1:5])
print(T[2:8])
print(T[2:9:3])
print(T[-1])
print(T[-5])
 

