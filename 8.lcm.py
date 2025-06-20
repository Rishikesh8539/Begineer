def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(number1, number2):
    return abs(number1 * number2) // gcd(number1, number2)

number1 = 12
number2 = 18
result = lcm(number1, number2)
print(f"LCM of {number1} and {number2} is: {result}")
