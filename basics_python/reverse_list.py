def reverse_list(lst):
    # Your code goes here
    ls = []
    for i in range(len(lst)-1,-1,-1):
        ls.append(lst[i])
    return ls

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(reverse_list(lst))  # Output: [5, 4, 3, 2, 1]