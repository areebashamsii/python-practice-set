# 1. Write a program to print a multiplication table of a given input:
table_num=int(input("Enter a number to print its Table:"))



for i in range (1,11):
  print(str(table_num)+" * "+str(i) ," = ",table_num*i )


# 2.Write a program to greet all the person names in a list that starts from "S":

name_list=["sam","sia","zara","sal","den","luci","sue"]


for name in name_list:

    if name.startswith("s"):
        print("Asslamualikum "+name)

# 3.Attempt problem 1 by using while loop:

enter_table=int(input("Enter a num to print its multiplication table:"))
i=1

while(i<=10):
    print(str(enter_table)+"*"+ str(i)+"=" ,enter_table*i)
    i+=1

# 4.Find that a given number is prime or not:
number=int(input("Enter number to check if it is prime or not:"))

for i in range (2,number):
     if (number%i)==0:
          print("It is not a prime number.")
     i+=1     
     break
else:
     print("Its  a prime number.")     
     

# 5. Print the sum of given natural numbers using while loop:
number1=int(input("enter a number:"))
i=0
sum=0
while(i<=number1):
    sum += i
    i+=1
print(sum)   

 

     
     
# 6. Find the factorial of a given number:
numb=int(input("Enter a num:"))
factorial=1
i=1
for i in range(1,numb+1):
    
    factorial = factorial*i

print(factorial)

# 7. print this star pattern n=3 ( it means three space in total) 
#   *
#  ***
# ******
n=int(input("Enter the number of Spaces:"))

for i in range(1,n+1):
    print(" "*(n-i) ,end="")
    print("*"*(2*i-1) ,end="")
    print("")

# 8 Draw this pattern 
#*
#**
#***

n2=int(input("Enter the number :"))

for i in range(1,n2+1):
    
    print("*"*(i) ,end="")
    
    print("")
     
# 9 Draw this pattern 
# ***
# * *
# ***

n3=int(input("Enter the number:"))

for i in range(1,n3+1):
    if (i==1 or i==n3):
     print("*"*(n3) ,end="")
    else:
        print("*",end="")
        print(" "*(n3-2),end="")
        print("*",end="")
    
    print("")
# 10 .print the given number reversed multiplication table by using for loop:
num4=int(input("Enter a Number:"))
i=10

for i in range (1,11):
 print(str(num4)+"*"+str(11-i)+"=",num4*(11-i))
 i-=1
