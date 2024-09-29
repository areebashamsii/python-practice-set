# 1. Craete a dictionary of urdu words as key and their english meanings as values in which a user can type a specif words and can check its meaning.

dict={
    "jannat":"heaven",
    "bheer":"crowd",
    "dukandaar":"shopkeeper",
    "tamasha":"fuss"
}

search=input("Type urdu word and check its meaning :")
print("The English word for " + search + " is" ,dict[search] ,".")

# 2. Take input of 8 integers and display all the unique no once ( no repetition) by using add() function:

setofint=set() # empty set is written in the () brackets and empty dictionary is written as {}:

int0=int(input("Enter integer :"))
setofint.add(int0)
int1=int(input("Enter integer :"))
setofint.add(int1)
int2=int(input("Enter integer :"))
setofint.add(int2)
int3=int(input("Enter integer :"))
setofint.add(int3)
int4=int(input("Enter integer :"))
setofint.add(int4)
int5=int(input("Enter integer :"))
setofint.add(int5)
int6=int(input("Enter integer :"))
setofint.add(int6)
int7=int(input("Enter integer :"))
setofint.add(int7)

print(setofint ,type(setofint))

# 3.Can we have 18 int and "18" string in a set?

set3={18,"18"} #yes we can have int 18 and strting 18 both in a set .
#Remember that set prints values in unordered manner , not like the original set (most of the time).
print(set3)

# 4.What will be the length of the following set:
s=set()
s.add(20)
s.add(20.0)
s.add("20")   #Its length is 2 because 20.0 is an int 
#which is same as int 20 so set will not count same value twice and "20 " string is different than 20 int. 
print(len(s))

# 5. Type of S={}:
S={}            #Its type is dictionary because empty set is written in the () brackets and empty dictionary is written as {}.
print(type(S))

# 6. Create an empty dictionary and allow four user to  enter their name as key and their favourite series as pair , assume that the names are unique.
favshows={}

name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})

print(favshows)

# 7.Check if 2 friends enter the same name on program 6 , what will happen?
favshows={}

name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")          # ANS : If the key  will be same then it will remove repeated keys and only print unique keys.But will print repeatd values .
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})
name=input("Enter your name:")
favshow=input("Enter your favourite Show:")
favshows.update({name:favshow})

print(favshows)

# 8. Can you change a value of a list that is contained in a set :
S={8,7,12,"areeba"}
S[4]=[3,4] # not possible because we cannot add a list into a set also you can do indexing in set.
print(S)