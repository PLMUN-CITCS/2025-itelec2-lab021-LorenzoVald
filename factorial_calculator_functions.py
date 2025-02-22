# Get user input
num = int(input("Enter a non-negative integer: "))

# Check if the input is valid
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Compute factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    # Print the result
    print("The factorial of", num, "is:", factorial)