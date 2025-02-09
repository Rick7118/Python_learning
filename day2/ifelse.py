#if
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")

#if-else
num=int(input("Enter a number:"))

if num%2==0:
    print("It is an even number!")
else:
    print("It is an odd number")

#if-elif-else
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
