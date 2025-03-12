"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
def find_missing_number(arr, n):
    """Finds the missing number in the given array."""
    total_sum = n * (n + 1) // 2  # Step 1: Calculate sum of first n numbers
    actual_sum = sum(arr)  # Step 2: Calculate sum of given numbers
    return total_sum - actual_sum  # Step 3: Find missing number

# Example usage
arr = [1, 2, 3, 5, 6]  # Given array
n = 6  # Total expected numbers
missing_number = find_missing_number(arr, n)
print("Missing number:", missing_number)  # Output: 4
