def generate_fibonacci(n):
    # Initial Fibonacci sequence
    fibonacci_sequence = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibonacci_sequence
    
    counter = 2

    while counter < n:
        # Calculate the next Fibonacci number
        temp = fibonacci_sequence[counter - 1] + fibonacci_sequence[counter - 2]
        fibonacci_sequence.append(temp)
        # Increase counter
        counter += 1

    return fibonacci_sequence


# Test the function with n = 8
check = generate_fibonacci(8)
print(check)
