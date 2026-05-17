def is_subset(lst1, lst2):
    # Your code goes here
    lst1 = set(lst1)
    lst2 = set(lst2)
    
    return lst1.issubset(lst2)

if __name__ == "__main__":
    lst1 = [1, 2, 3]
    lst2 = [3, 2, 1, 4, 5]
    print(is_subset(lst1, lst2))  # Output: True