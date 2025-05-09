
def fibonacci(n):
    if n <= 0:
        return "Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Enter the position of (n) fibonacci number: "))
print(f"The {n}th fibonacci number is: {fibonacci(n)}")
