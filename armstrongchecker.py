#Armstrong Number Checker

n = int(input("Enter a number: "))

num = n
digits = len(str(n))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")