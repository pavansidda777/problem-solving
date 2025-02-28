# check whether a number is positive or negative or zero
n=int(input("enter a number:"))
if n < 0:
    print("the number is negative")
elif n == 0:
    print("the number is zero")
else:
    print("the number is positive")




# check whether a given number is even or odd
n1=int(input("enter a number:"))
if n1 == 0:
    print("enter a valid number")
elif n1%2 == 0:
    print("number is even")
else:
    print("number is odd")




# check if a person is eligible to vote or not
n2=int(input("enter age:"))
if n2 == 0:
    print("invalid")
elif n2 < 18:
    print("not eligible")
elif n2 >= 18:
    print("eligible")
 





# check greatest of two numbers

n3=int(input("enter a number1:"))
n4=int(input("enter a number2:"))

if (n3 == n4):
    print("equal")
elif n3>n4:
    print("n3 is greater",n3)
else:
    print(" n4 is greater",n4)








# check scores of a student
marks=int(input("enter the marks:"))

if marks == 0:
   print("not valid")
elif marks >= 40:
    print("pass")
else:
    print("fail")






# based on number print name of the day

n5=int(input("enter number:"))
if n5 <= 0:
    print("not valid")
elif n5 == 1:
    print("monday")
elif n5 == 2:
    print("tuesday")
elif n5 == 3:
    print("wednesday")
elif n5 == 4:
    print("thursday")
elif n5 == 5:
    print("friday")
elif n5 == 6:
    print("saturday")
elif n5 == 7:
    print("sunday")





# simple calculator
operation=input("perform calculation:")
n6=int(input("enter number1:"))
n7=int(input("enter number2:"))
if operation == "+":
    print(n6+n7)
elif operation == "-":
    print(n6-n7)
elif operation == "*":
    print(n6*n7)
elif operation == "/":
    if n7 == 0:
        print("division by zero is not possible")
    else:
         print(n6/n7)


# display the name of the month
monthnum=int(input("enter month number:"))
if monthnum == 1:
    print("january")
elif monthnum == 2:
    print("february")
elif  monthnum == 3:
    print("march")
elif monthnum == 4:
    print("april")
elif monthnum == 5:
    print("may")
elif monthnum == 6:
    print("june")
elif monthnum == 7:
    print("july")
elif monthnum == 8:
    print("august")
elif monthnum == 9:
    print("september")
elif monthnum == 10:
    print("october")
elif monthnum == 11 :
    print("november")
elif monthnum == 12:
    print("december")
else :
    print("invalid")





# greatest of three numbers
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))
if (num1>num2) & (num1>num3):
    print(num1)
elif (num2>num1) & (num2>num3):
    print(num2)
else:
    print(num3)


# leap year or not
leap=int(input("enter year:"))
if leap == 0:
    print("invalid")
elif (leap%400 == 0) or (leap%4 == 0 and leap%100 !=0):
    print("it is a leap year")
else:
    print("not leap year")






# vowel or consonant
n8=input("enter character:").lower()
if len(n8) == 1:
    if n8 in ['a','e','i','o','u']:
        print("given char is vowel")
    elif n8.isalpha():
        print("consonant")
else:
    print("invalid")

# grade of a student
marks=float(input("enter marks:"))
if marks<=0:
    print("enter valid marks")
elif (marks>=90) and (marks<=100):
    print("grade A")
elif (marks>=80) and(marks<=89):
    print("grade B")
elif (marks<=70):
    print("fail")





# to find triangle 
a=int(input("enter side1:"))
b=int(input("enter side2:"))
c=int(input("enter side3:"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("triangle is possible")
else:
    print("triangle is not possible")



# sum of digits using while loop
n9=123456
sum=0
while n>0:
    rem=n9%10
    sum += rem
    n9=n9//10
print(sum)

# count no of digits in a number

d=1234567890
cnt=0
while d>0:
    rem=d%10
    cnt += 1
    d=d//10
print(cnt)












    
# divisible by 3 and 5
nd=int(input("enter the number:"))
for i in range(1,nd+1):
    if i%5==0:
        print(i,"divisible by 5")
    if i%3==0:
        print(i,"divisible by 3")



