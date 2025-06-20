num = 12345
revnum = 0

while num > 0:
    revnum = revnum * 10 + num % 10
    num //= 10

print(f"revnum = {revnum}")
v
