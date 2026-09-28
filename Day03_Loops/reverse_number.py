# reverse_number.py

def reverse_number_string(n):
    # Handle negative numbers
    sign = -1 if n < 0 else 1
    
    # Convert to string, remove minus sign if present, reverse, and convert back
    reversed_int = int(str(abs(n))[::-1])
    
    return sign * reversed_int

# Example usage
number = -5821
print(f"Original: {number} -> Reversed: {reverse_number_string(number)}")
