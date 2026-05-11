def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    if (len(keys) != len(values)):
        return False
    return dict(zip(keys,values))

if __name__ == "__main__":
        
        keys = ['a', 'b', 'c'] 
        values = [1, 2, 3]
        print(merge_lists_to_dictionary(keys,values))



