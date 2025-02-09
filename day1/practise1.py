#Basic print and variables
print("python is fun")

name="Rick"
age="21" #age is stored as a string as you can only concatenate strings
city="Kolkata"

print("My name is "+name+" and i am "+age+" years old. I was born in "+ city)

#Basic Data types and their operations
num1=34
num2=32
num3=19.2
num4=9.11

print(num1+num2)
print(num3-num4)
print(num1*num3)
print(num1%num4)

#comparison operator
num=int(input("Enter a number: "))
print(num>10) #python can see right through your bullshit and tell you if its true or flase
 
#userinput
birthYear=int(input("Enter your birthyear: "))
age=2025-birthYear

print(f"You are {age} years old") #using fstring is more efficient


