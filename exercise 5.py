n = int(input("Enter a positive integer: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
string = str(factorial)
count = 0
for char in reversed(string):
    if char == '0':
        count += 1
    else:
        break
print(f"The factorial of the number is: {factorial}")
print(f"The number of trailing zeros in the factorial is: {count}")
