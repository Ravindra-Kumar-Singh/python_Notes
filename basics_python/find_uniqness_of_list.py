def check_unique(lst):
    # Your code goes here
    lst1 = set(lst)
    lst_unique = list(lst1)
    
    if len(lst) == len(lst_unique):
        return True
    else:
        return False
    
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(check_unique(lst))  # Output: True

    lst = [1, 2, 3, 4, 5, 1]
    print(check_unique(lst))  # Output: False