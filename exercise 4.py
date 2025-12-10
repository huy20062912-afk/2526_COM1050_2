n = int(input("Enter a positive integer: "))
if n < 6 or n % 3 == 1 or n % 3 == 2:
    print("Input is not sum of 3 consecutive integers")
else:
    x = n // 3
    print(f"The three consecutive integers are: {x-1}, {x}, {x+1}")