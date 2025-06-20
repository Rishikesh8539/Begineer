def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

num = 987
initial_sum = sum(int(digit) for digit in str(num))
final_result = sum_of_digits(initial_sum)

print(f"Sum_of_digits = {initial_sum}, Final Output: {final_result}")
