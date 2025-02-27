#print 1-100 numbers
for i in range(1, 101):
    print(i)

#natural numbers
num= int(input("Enter a number: "))
sum_n = 0
for i in range(1, num + 1):
    sum_n += i
print("Sum of first", num, "natural numbers:", sum_n)

#even numbers in 1-50
num2=2
while num2 <= 50:
    print(num2)
    num2 += 2

#multiplication table
num3 = int(input("Enter a number: "))
print("Multiplication table for", num3)
for i in range(1, 21):
    print(num3, "x", i, "=", num3 * i)

#factorial
num4= int(input("Enter a number: "))
factorial = 1
i = num
while i > 0:
    factorial *= i
    i -= 1  
print("Factorial of", num4, "is", factorial)

#divisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: 
        print(i)
