input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = ' '.join(input_sentence.split()[::-1])
print(f"Output after reverse = \"{output_sentence}\"")
