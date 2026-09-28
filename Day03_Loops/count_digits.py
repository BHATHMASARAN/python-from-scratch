# count_digits.py

def count_digits_str(n):
    # Convert absolute value to string to ignore negative signs
    return len(str(abs(n)))

# Example usage
number = -48291
print(f"The number of digits in {number} is: {count_digits_str(number)}")
