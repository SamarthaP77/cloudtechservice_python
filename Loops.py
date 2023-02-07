#Forloop

for letter in 'Basketball':
 print('Current letter is: ', letter)

for z in range(20):
    print("Football")

#whileloop
count = 0
while count <10:
    print("The count is", count)
    count = count+1

food = 10
while food<90:
    print('food')
    food+=10
for a in range(8,60,8):
    print(a)

#Nestedloop
for i in range(1,6):
  for j in range (1,i+1):
      print (j, end=" ")
  print()

for i in range(1,6):
    for j in range(1,5):
        print("football")


#Break statement
for i in range(20,40):
    if i==35:
        break
    print(i)

#Continue statement
for j in range(6,20):
    if j==17:
        continue
    print(j)

#Pass statement
for a in range(6,20):
    if a==17:
        pass
    print(a)

#List
    #Accesing values in list
L=[9,18.8,'Hi',15.99,'School',100]
print(L[5])
print(L[2:4])
print(L[-2])
print(L[3])


    
    


