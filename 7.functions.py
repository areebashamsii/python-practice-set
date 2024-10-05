# Quick Quiz:
# Create a fucntion to say "Good Morning!" to th person:

def say_good_morning():  # def is called function definition.
    name=input("Enter your name:")
    print("Good Morning " +name +"!")
say_good_morning()   # This is called "function call" .function name and parenthesis is used to call the function.
say_good_morning()  
say_good_morning()  
say_good_morning()  
print("Good Morning to you all.")  

# 1. Write a function to find the greatest of three numbers:

def find_greatest_num():
    n1=int(input("Enter NUM 1:"))
    n2=int(input("Enter NUM 2:"))
    n3=int(input("Enter NUM 3:"))
    if(n1>n2 and n1>n3):
        print(str(n1)+' is the greatest integer.')
    elif( n2>n1 and n2>n3):
        print(str(n2)+' is the greatest integer.')
    elif( n3>n1 and n3>n2):
        print(str(n3)+' is the greatest integer.')   
    else:
        print('Enter valid numbers to compare!')  
find_greatest_num()          

# 2. Create a function to  convert celsius into farnhite :
# formula: F=(C*9/5)+32
def celsius_to_farenhite():
    celsius=int(input("Enter degrees in celcius:"))
    farenhite=(celsius*9/5)+32
    print(farenhite)

celsius_to_farenhite()   

# 3.How you prevent print() function to print new line:
print("My" , end="")
print("Name" , end="")  # , end="" prevents the print() function to go to next line.
print("is", end="")
print("Areeba Shamsi", end="")

#Output:
# My Name is Areeba Shamsi

# 4.Write a recursive function ( A function that call it self when needed to do some logic in the code) to calculate the sum of "n" natural numbers:
''' 
sum of natural number(1)=1        In recursive function you have to check the process and have to made thee formula out of it.
sum of natural number(2)=1+2
sum of natural number(3)=1+2+3      
sum of natural number(4)=1+2+3+4
sum of natural number(5)=1+2+3+4+5   n-1+n...........


'''



def sum_of_naturalnum(num): #this is called parameter that takes argument in it. 
    if num==1:  #base value
        return 1
    return sum_of_naturalnum(num-1) + num    #recursive value.

sum=sum_of_naturalnum(22)   #function with argument.
print(sum)

# 5.write a function to print first n lines of following pattern where n=given number:
# ***  n
# **   n-1
# *    n-1

def pattern(n):
    if n==0:
        return 
    print("*"*n)
    pattern(n-1)
    

pattern(20)

# 6. Create a function that converts inch to cm :
#formula :  cm=inch X 2.54

def inch_to_cm():
    inch=int(input("Enter measurement in inches:"))
    cm=inch*2.54
    return cm

centimeter=inch_to_cm()
print(centimeter)

# 7.create a function that removes a given word from the list and strip it at the same time:

names=["areeba","sora","ben","claire","goku"]
def remove_name():

    name=input("Enter a name to remove it from the list:")
    if name in names:
        names.remove(name) 
    else:
        print("Name is not in the list!")
    return names


newlist=remove_name()
print(newlist)
    
# 8.Create a function that prints  multiplication table of a given number:
def table():
    table_num=int(input('Enter a nunber to prints its multiplication table:'))
    for i in range (1,11):
        print(str(table_num)+"*" + str(i) + " = " + str(i*table_num))
     

table()


 