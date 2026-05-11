def largest_element(numbers):
    if not numbers:
        return None  # Return None for an empty list
    if len(numbers) == 1:
        return numbers[0]  # Return the only element if the list has one element

    largest = numbers[0]  # Initialize largest with the first element
    #numbers = set(numbers) # Convert list to set to remove duplicates
    # for num in numbers:
    #     if num > largest:
    #         largest = num  # Update largest if current number is greater

    #numbers = list(numbers)  # Convert set back to list
    numbers.sort(reverse=True)  # Sort the list in descending order
    print("the list element after sort:", numbers)
    largest = numbers[0]  # The first element will be the largest after sorting
    return largest

if __name__ == "__main__":
    numbers = [10, 20, 9, 10, 15,50,50]
    print(numbers)
    print("The largest element in the list is:", largest_element(numbers))