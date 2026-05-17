def is_prime(n):
    if n <= 1:
        return False
    """Check for factors from 2 to the square root of n. if factors divde n then it is not 
    prime number else number is prime number"""
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = 10
    print(is_prime(n))  # Output: True