#Tuples
T1 = (990,67,'ok','food')
T2 = ('water',88,76,56)
T3 = T1 + T2
print(T3)

#Deleting Tuple
tup = ('Math', 'English', 85, 100)
del tup

#Example of Tuple function

li = (10,20,30,90)
print(len(li))
print(max(li))
print(min(li))

#Tuple Methods
d = (20,15,'Hello','Python',10)
print(d.count(10))
print(d.index(10))

#Slicing
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

#Iterating through a Tuple in Python
sports= ('football', 'Basketball', 'Volleyball')
for sport in sports:
    print(sport)
#Check if an Item Exists in the Python Tuple
languages = ('Python', 'Swift', 'C++')
print('C' in languages)    # False
print('Python' in languages)    # True

#Dictionary
#Accesing values in dictionary
D = {'Name':'Samartha','Age':'23','Gender':'Male'}
print(D['Name'])
print(D['Age'])
print(D['Gender'])

#Updating Dictionary
D = {'Name':'Samartha','Age':23,'Degree':'Bachelors'}
D['Age'] = 30 #updating existing entry
D['School'] = 'Kendriya Vidhyalaya'#adding new entry
print(D)
#Deleting dictionary elements
D = {'Name':'Samartha','Age':23,'Degree':'Bachelors'}
del D['Name']
print (D)
#remove all entires in the dictionary
D.clear()
print(D)
#Delete entire dictionary
del D
#print(D)


#Dictionary Functions
E = {1:20,2:30,3:40}
print(len(E))
print(str(E))
print(type(E))




