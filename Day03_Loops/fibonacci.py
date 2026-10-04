# fibonacci.py

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Generate the remaining terms
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

# Example: Generate the first 10 Fibonacci numbers
terms = 10
print(f"The first {terms} terms of the Fibonacci sequence are:")
print(generate_fibonacci(terms))
