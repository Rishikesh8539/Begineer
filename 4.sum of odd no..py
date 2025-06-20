def sum_of_odd_numbers(start, stop):
    total_sum = 0
    
    for number in range(start, stop + 1):
        if number % 2 != 0:  # Check if the number is odd
            total_sum += number
            
    return total_sum

start = 1
stop = 10
result = sum_of_odd_numbers(start, stop)
print(f"Sum of odd numbers between {start} and {stop}: {result}")
