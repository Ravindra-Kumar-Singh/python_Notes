def sum_of_even_numbers(n):
    """This function takes a natural number n as input and returns the sum of all even numbers from 1 to n."""
    if n < 1:
        return 0  # Return 0 for non-positive integers
    even_sum = lambda n: sum(i for i in range(1, n*2 + 1) if i % 2 == 0)
    return even_sum(n)

if __name__ == "__main__":
    n = 4
    print(sum_of_even_numbers(n))  # Output: 20 (2 + 4 + 6 + 8)