def merge_two_sorted_lists(list1: list, list2: list):
    # Your code goes here
    i,j = 0,0

    list1 = sorted(list1)
    list2 = sorted(list2)
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            list2[j] < list1[i]
            merged_list.append(list2[j])
            j += 1

    #     # If there are remaining elements in list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    #     # If there are remaining elements in list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

    
if __name__ == "__main__":      
    list1 = [1, 3, 5,8,7,9]
    list2 = [2, 4, 6]
    print(merge_two_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6,7,8,9]   