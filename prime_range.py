"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
def print_primes(start, end):
    """Print all prime numbers in the given range."""
    for num in range(max(2, start), end + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num, end=", ")

# Take user input
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end}:")
print_primes(start, end)
