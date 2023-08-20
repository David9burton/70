def factorial(n):
    """Return the factorial of a non-negative integer."""
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
while True:
    try:
        number = int(input("Enter a non-negative number:"))
        if number < 0:
            raise ValueError
        print(f"Factorial of {number} is {factorial(number)}")
        break
    except ValueError:
        print("Please enter a valid non-negative number.")
        