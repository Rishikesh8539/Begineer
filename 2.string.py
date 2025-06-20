def count_letters_and_digits(input_string):
    letters_count = 0
    digits_count = 0
    
    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
            
    return letters_count, digits_count
user_input = input("Enter a string: ")
letters, digits = count_letters_and_digits(user_input)
print(f"Alphabets: {letters} & Number: {digits}")
