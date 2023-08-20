def find_divisors(num):
    """Return a list of divisors of a positive integer."""
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

while True:
    try:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            raise ValueError
        print(f"Divisors of {number} are: {find_divisors(number)}")
        break
    except ValueError:
        print("Please enter a valid positive number.")
number = int(input("Enter a number: "))
print(f"Divisors of {number} are: {find_divisors(number)}")