a="My name is Rick"
print(a)

#multiline string using triple quotes

multilineString='''This is a 
multiline string
ya feel me bitch ?
                    '''

print(multilineString)

#concatenation
str1="Hello"
str2="World"

concatenated=str1+" "+str2
print(concatenated)

#stringlength
string_len="python"
my_length=len(string_len)
print(my_length)

print(len("MAchine Learning"))

#String Indexing and Slicing
text="Python"
first_char=text[0]#you already know this shit bro
substring=text[0:4]#gives you 0 to 3
print(first_char)
print(substring)

#string formatting
name="Rick"
age=21

formattedString=f"My name is {name} and i am {age} years old" #this is called a f-string
print(formattedString)

#escape characters or sequences
#this bothered me a lot back when i was learning python for the first time

escaped_string="This is a line. \nThis is a new line"
print(escaped_string)

