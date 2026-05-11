def rotate_list(lst, k):
    # Your code goes here
    for i in range(k):
        lst.append(lst.pop(0))
    return lst

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    k = 2
    print(rotate_list(lst, k))  # Output: [3, 4, 5, 1, 2]