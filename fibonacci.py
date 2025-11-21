def fibonacci(n):
    # Function to print first n Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Main program
try:
    N = int(input("Enter a value for N (N > 0): "))

    if N <= 0:
        print("Error: N must be greater than 0.")
    else:
        print("Fibonacci sequence:")
        fibonacci(N)

except ValueError:
    print("Error: Please enter a valid integer.")
