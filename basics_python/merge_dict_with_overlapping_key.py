def merge_dicts_with_overlapping_keys(dicts):
    """this function merge multiple dict with overlapping keys and sum the 
    values of the overlapping keys"""

    """Loop though all the dict
    """
    merged_dict = {}
    for dict in dicts:
        """Loop through all the key values of all the dicts"""
        for key, value in dict.items():
            """"if key is already in the merged_dict then add value to the existing key value"""
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value

    return merged_dict

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    dict3 = {'c': 5, 'd': 6, 'e': 7}

    dicts = [dict1, dict2, dict3]
    print(merge_dicts_with_overlapping_keys(dicts))  
    # Output: {'a': 1, 'b': 5, 'c': 12, 'd': 11, 'e': 7}

