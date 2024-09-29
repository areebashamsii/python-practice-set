# 1 ADD TWO NUMBERS:
num1=int(input("Enter first Number:"))
num2=int(input("Enter Second Number:"))

result=int(num1+num2)
print(" sum of "+  str( num1) +" and "+ str( num2) +" is "+ str( result))

# by adding str() while concatinating is important because it only concatinate if it is string so we have to type cast int into str


# 2 DIVIDE NUMBER AND PRINT REMAINDER:

numb1=int(input("Enter Number:"))
numb2=int(input("Enter Number to divide with: "))
result2=int(numb1%numb2)
print(" The Remainder of "+str(numb1)+ " Divided by "+str(numb2)+" is "+str(result2))

# 3 CHECK THE GIVEN VALUE'S DATA TYPE:

checkdatatype=input("Enter any value to check its data type:")
result3=type(checkdatatype)
print(" The data type of your given value is "+str(result3)) 

#input function returns string data type so for finding all data types there is another method but this also correct.


# 4 FIND AVERAGE OF 3 NUMBERS:


number1=int(input("Enter First Number:"))
number2=int(input("Enter Second Number:"))
number3=int(input("Enter Third Number:"))
average=(number1+number2+number3)/3
print("Average of "+ str(number1)+" , "+str(number2)+" and "+str(number3) +" is " + str(average))

# 5 CALCULATE THE SQUARE OF USER INPUT:


numBer=int(input("Enter Number to Calculate its Square:"))
result5=numBer**2
print("The Square of "+str(numBer)+" is "+str(result5))