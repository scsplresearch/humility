def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

### GPT ###
def factorial(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


x = int(input("factorial(x): x = "))
print(factorial(x))
