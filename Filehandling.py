file = open('Ok.txt','r')
for x in file:
    print(x)
file.close()    
    
print(file.name)    
print(file.mode)
print(file.closed)

#Not specifying the file mode
file1 = open('Hello.txt')
for x in file1:
    print(x)
file.close()    
print(file.mode)    
print(file.closed)

#Read Mode() Character wise
file2 = open('Hello.txt','r')
print(file2.read(20))

#Creating a file using write() method
file3 = open('Ok.txt','w')
file3.write("I am 23 years old")
file3.close()

#Working of Append mode()
file4 = open('Ok.txt','a')
file4.write("Spring season is almost here")
file4.close()

#File Positions
fo = open("Hello.txt","r+")
str = fo.read(5)
print("Read String is : ",fo)

#To find the current file position
position = fo.tell()
print("Current position is : ",position)

#Repositioning the pointer at the beggining again
position = fo.seek(0,0)
str = fo.read(5)
print("Again string is : ",str)

#Renaming a file method()
import os
os.replace("Hello.txt" ,"pal.txt")

#Removing a file
import os
os.remove("ok.txt")







    