def triangles(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b != c or a == c != b or b == c != a:
        return "Isosceles"
    elif a == b == c:
        return "Equilateral"
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return "Right-angled"
    else: 
        return "Normal triangle"
try:
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = float(input("Enter length of side c: "))
    result = triangles(a, b, c)
    print(result)
except ValueError:
    print("Please enter valid numbers")
        