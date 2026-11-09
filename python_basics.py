#variables

name="roshani"
age=20
height=5.7
is_student=True
print(name)
print(age)
print(height)
print(is_student)

#checking data types

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#operators

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%3)
print(a//3)
print(2**3)

#taking user input

name=(input("enter your name:"))
print("hello",name)

#datatype , input
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
print("addition=",num1+num2)

#conditional statements if else

age=12
if age>=18:
    print("you can vote")
else:
    print("you cannot vote")


#if-elif-else statment
marks=67
if marks>=90:
    print("a grade")
elif marks>=60:
    print("b grade")
else:
    print("c grade")

#user input for if else condition

marks=int(input("enter marks:"))
if marks>=90:
    print("a grade")
elif marks>=60:
    print("b grade")
else:
    print("c grade")

#for loop

for i in range(5):
  print(i)

#while loop
i=1
while i<=4:
    print(i)
    i=i+1
    
name="roshani"
city="pune"
message="hello world"

#string operations
#concatenation

first="roshani"
last="chourasiya"
fullname=first+" "+last
print(fullname)

#string length

name="roshani chourasiya"
print(len(name))

#uppercase and lowercase

name="roshani"
print(name.upper())
print(name.lower())

#replacing characters

message="hello roshani"
print(message.replace("hello","welcome"))

