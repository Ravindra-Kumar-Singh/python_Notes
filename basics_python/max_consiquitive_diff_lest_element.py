def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0  # No consecutive elements, so return 0
    max_diff = 0
    for i in range(1,len(lst)):
        diff = abs(lst[i] - lst[i-1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

if __name__ == "__main__":
    lst = [1, 3, 6, 10]
    print(max_consecutive_difference(lst))  # Output: 4 (difference between 6 and 10)