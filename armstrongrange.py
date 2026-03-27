# Armstrong Number Checker

# n = int(input("Enter a number: "))

# num = n
# digits = len(str(n))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum += digit ** digits
#     num //= 10

# if sum == n:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")



    # Print Armstrong numbers in a range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for n in range(start, end + 1):
    digits = len(str(n))
    sum = 0
    temp = n

    while temp > 0:
        digit = temp % 10

        sum += digit ** digits
        temp //= 10

    if sum == n:
        print(n, end=" ")