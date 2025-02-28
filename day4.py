#approach1 for prime numbers
num1=int(input("enter a number which is prime:"))
count=0
for i in range(1,num1+1):
    if num1%i==0:
        count+=1
if count == 2:
    print("its prime number")
else:
    print("its not aprime number")


#approach2

num1=int(input("enter a number which is prime:"))
if num1 in [0,1]:
    print("its not a prime")
elif num1<0:
    print("invalid number")
else:
    spy=False
    for i in range(2,num1):
        if num1%i==0 :
            spy=True
            print("its not prime")
            break
    if spy == False:
        print("prime number") 

#approach3
# m=a*b
#b=1 then a is m
#b=2 then a is m/2
#b=3 then a is m/3



num1=int(input("enter a number which is prime:"))
if num1 in [0,1]:
    print("its not a prime")
elif num1<0:
    print("invalid number")
else:
    spy=False
    for i in range(2,(num1//2)+1):
        if num1%i==0 :
            spy=True
            print("its not prime")
            break
    if spy == False:
        print("prime number") 

#approach4
#by square roots of the number


num1=int(input("enter a number which is prime:"))
if num1 in [0,1]:
    print("its not a prime")
elif num1<0:
    print("invalid number")
else:
    spy=False
    for i in range(2,int(num1**0.5)+1):
        if num1%i==0 :
            spy=True
            print("its not prime")
            break
    if spy == False:
        print("prime number") 

# menu-driven program -square,cube,exist
while True:
    print("square - cube - exist")
    user_input=input("enter option:").lower()
    if user_input == "square":
        user_sq_number=float(input("enter the num of square"))
        print(user_sq_number*2)
    elif user_input == "cube":
        user_cube_number=float(input("enter the num of cube"))
        print(user_sq_number*3) 
    elif user_input == "exist":
        break
    else:
        print("invalid input")



# userlogin and user password

db_user_username = "Pavan"
db_user_password = "pavan sidda"
total_attempts=3
while total_attempts > 0:
    input_username=input("enter username:")
    input_password=input("enter password:")
    if input_username == db_user_username and input_password == db_user_password:
       print("login successful")
       break
    else:
        total_attempts -= 1
        print("wrong username/password","u still have",total_attempts,"attempts")


# factorial of a given number

n=int(input("enter a number to find factorial:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i += 1
    print(fact)


# fibonacci series

n=int(input("enter range:"))
first=0
second=1
for i in range(1,n+1):
    print(first)
    next=first+second
    first=second
    second=next


 







