# 1. Say Good Morning to individual:
name= input("Enter Your name :")
print(f"Good Morning {name}!")  # f is used to show that input is string.



# 2.Replace the name and date from this code :

#Before:
letter='''  Dear <|Name|> ,
 You are Selected !
  <|Date|>
 '''
#After:

letter='''  Dear <|Name|> ,
 You are Selected !
 <|Date|>
'''
print(letter.replace("<|Name|>","Areeba Shamsi").replace("<|Date|>","27-09-2024"))



# 3.Write a program to detect double space:

Name="areeba   shamsi"
print(Name.find("  ")) # If there will be double space it will show its index otherwise
#it will show -1 which means there is no double space or any speecific element of the variable



  # 4. Replace double spaces from Problem three:
Name2="areeba  shamsi"
print(Name2.replace("  "," "))



 # 5. Format the text by using escape sequence:
# Before:
line="Dear Areeba , this python course is nice. Thanks."
# After
formating="Dear Areeba ,\n \t this python course is nice.\n  Thanks."
print(formating)

