#strings
str1="The language 'Python' is named after Monty Python,not the snake"
str2="Python's strength is its diverse and supportive community"
print(str1)
print(str2)

 #changing case in strings
name="subhayu sengupta"
print(name.title())

name="Subhayu Sengupta"
print(name.upper())
print(name.lower())

#concatenation
firstName="subhayu"
lastName="sengupta"
fullName=firstName+" "+lastName
print(fullName)

print("Hello, " + fullName.title() + "!")

#space and new line
print("Language that i know: \n\tPython\n\tC\n\tCpp ")

#stripping empty space

lang = "   python  "

print(lang.lstrip())  #all left spaces deleted
print(lang.rstrip())  #all left spaces deleted
print(lang.strip())   #all left spaces deleted

age=23
message="Happy" + str(age) + "rd Birthday!" #you cant concatenate int with sring
print(message)