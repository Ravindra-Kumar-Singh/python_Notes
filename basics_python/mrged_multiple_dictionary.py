def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    
    dict = [dict1,dict2,dict3]
    merged = {}
    for d in dict:
        merged.update(d)
    
    return merged

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'f': 6}

    print(merge_three_dictionaries(dict1, dict2, dict3))  # Output