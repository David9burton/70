def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

number = int(input("Enter a number: "))
print(f"Divisors of {number} are: {find_divisors(number)}")