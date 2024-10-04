# Quiz of ch#6 ( write a program to print yes if the user enter 18 or 18 above else no)
age=int(input("Enter Your Age:"))

if (age>=18):
    print("Yes!")
else:
    print("No!")




# # 1. Write a program to find the greatest of four numbers entered by the user:

int1=int(input("enter first int:"))
int2=int(input("enter  second int:"))
int3=int(input("enter third int:"))
int4=int(input("enter four int:"))

if (int1>int2) and (int1>int3) and (int1>int4):
    print("Int 1 is greater!")    
elif (int2>int1) and (int2>int3) and (int2>int4):
    print("Int 2 is greater!")  
elif (int3>int1) and (int3>int2) and (int3>int4):
    print("Int 3 is greater!")
elif (int4>int1) and (int4>int2) and (int4>int3):
    print ("Int 4 is greater!")
else:
    print("Input is invalid")
    
 # 2 .Take input from a student of 3 subjects marks and find the percentage of each subject and total percentage and print if it he is fail or pass :

total_marks=300
each_sub_Total_marks=100


eng_marks=int(input("Enter your english marks:"))
math_marks=int(input("Enter your maths marks:"))
science_marks=int(input("Enter your science marks:"))

obtained_marks= eng_marks+math_marks+science_marks



percentage_eng= eng_marks/each_sub_Total_marks*100
percentage_math= math_marks/each_sub_Total_marks*100
percentage_science= science_marks/each_sub_Total_marks*100

percentage=obtained_marks/total_marks*100

if(eng_marks>=33 and math_marks >=33 and science_marks>=33):
    print("congratulations ! you are passed in All subject")
else:
    print("You are fail in atleast one subject!")
print(percentage)    

# 3. Detect a spam comment :
spam_comments =["click this!","subscribe this!","Make alot of Money!","Buy Now!"]
comment=input("Enter a comment and check spam:")



if(comment in spam_comments):
    print("This is a Spam Comment")
else:
    print("This is not a Spam Comment")    

#4.Check if the username contains less than 10 characters or not:
    
user_name=input("Enter your username:")
len_of_username=len(user_name)
if(len_of_username <= 10):
    print("Your username has less than 10 character!")
else:
    print("Your username has more than 10 characters!")   

#5.find out weather the name is in the list or not:

list_of_names=["areeba","manahil","khola","esha"]
name=input("Enter your name:")

if(name in list_of_names):
    print("your name is in the list")
else:
    print("your name is not in the list")    

# 6. Assign grade :

percentage=int(input("Enter your percentage:"))    

if (percentage >=90 and percentage<100):
    print("Congratulations You got A* Grade!")
elif (percentage >=80):
    print("Congratulations You got A Grade!")
elif (percentage >=70):
    print("Congratulations You got B Grade!")  
elif (percentage >=60):
    print("Congratulations You got C Grade!")
elif (percentage >=50):
    print("Congratulations You got D Grade!")
elif(percentage<50 and percentage >0):
    print("you got F Grade!")   
else:
    print("You are entering invalid percentage")     

# 7.check if the gievn post is about elections or not:
post=input("Enter post discription :")
detect="elections"

if (detect in post):
    print("yes ! This post is about elections.")
else:
    print("No! This post is not about elections")    












