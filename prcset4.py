 # 1. Take input of 7 fruits and create a list out of it by using  append() function:
f1=input("Enter fruit 1:")
f2=input("Enter fruit 2:")
f3=input("Enter fruit 3:")
f4=input("Enter fruit 4:")
f5=input("Enter fruit 5:")
f6=input("Enter fruit 6:")
f7=input("Enter fruit 7:")
fruit=[] #list is written in the square bracket.



fruit.append(f1)
fruit.append(f2)
fruit.append(f3) # name.append function is used to add values in the end of the list.
fruit.append(f4)
fruit.append(f5)
fruit.append(f6)
fruit.append(f7)
print(fruit)


 # 2. Take input of 6 students marks and print them in a sorted order by using sort() function.
S1=input("Enter Your Marks 1:")
S2=input("Enter Your Marks 2:")
S3=input("Enter Your Marks 3:")
S4=input("Enter Your Marks 4:")
S5=input("Enter Your Marks 5:")
S6=input("Enter Your Marks 6:")
S7=input("Enter Your Marks 7:")

marks=[]

marks.append(S1)
marks.append(S2)
marks.append(S3)
marks.append(S4)
marks.append(S5)
marks.append(S6)
marks.append(S7)

marks.sort()
print(marks)

# In this method the output will be sort with alphabetical order like first it wirte 1's values then valus start from two then three and so on 
# to solve this issue we change the variable type from string to int.

S1=int(input("Enter Your Marks 1:"))
S2=int(input("Enter Your Marks 2:"))
S3=int(input("Enter Your Marks 3:"))
S4=int(input("Enter Your Marks 4:"))
S5=int(input("Enter Your Marks 5:"))
S6=int(input("Enter Your Marks 6:"))
S7=int(input("Enter Your Marks 7:"))

marks=[]

marks.append(S1)
marks.append(S2)
marks.append(S3)
marks.append(S4)
marks.append(S5)
marks.append(S6)
marks.append(S7)

marks.sort()
print(marks)

# 3. Check that tuple cannot be changed in python:

Tuple2=("areeba", 2 ,  True)

print(Tuple2.pop(1))         
print(Tuple2)           # This program will not return as tuples are mutable. 


# 4. Write a Program to Sum a list with four numbers by using sum(name) function:

list=[2,4,8,5,3]
sum= sum(list)
print(sum)

# 5.Write a program to count the no of zeroes in the tuple by using count function:
tuple1=(2,7,0,3,0,9,0,0,1,0)
count=tuple1.count(0)           # Tuples are mutable meaning that they do not change their original content , you have to assign them in different variable.
print(count)                    # name.Count(element) function is used to count a specific element in the tuple.

