#str.upper() &str.lower()

text="Hello, world!"
upper_text = text.upper()
lower_text = text.lower()

print(upper_text)
print(lower_text)

#str.capitalize() and str.title()

phrase="python pls help me get a job"

cap_phrase=phrase.capitalize() #firstwordforstletter
print(cap_phrase)

title_phrase=phrase.title() #firstlettereveryword
print(title_phrase)

#str.strip() , str.lstrip(), and str.rstrip()

sentence="    Python is fun!        "
a=sentence.rstrip() #removes empty spaces from the str....left right or bothing
print(a)

#str.startswith(prefix) and str.endswith(suffix)
filename="example.text"
starts_with=filename.startswith("example")
ends_with=filename.endswith("txt")
print(starts_with) #pretty self-explanatory
print(ends_with)

#str.replace(old,new)
sentence="I like programming in Cpp"

newSentence=sentence.replace("Cpp","Python")
print(newSentence)

#str.find(substring) and str.index(substring)
j="is powerful and python is easy to learn"
index1=j.find("python")
index2=j.index("python")
print(index1)
print(index2)

#str.split(seperator)

j="is powerful and python is easy to learn"
q=j.split(" ") #splits the string whenever the given seperator is identified in it (in this case the seperator is space(" "))
print(q)

#str.count(substring)
porqui="Python is the language i am learning right now because i kinda fuck with machine learning and maths . Python gang wassup. Me and my homies love Python heheheheh"
count=porqui.count("Python")
print(count)