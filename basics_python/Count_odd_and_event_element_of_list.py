def count_even_odd(lst):
    # Your code goes here
    even_count = 0
    odd_count = 0
    list_even = []
    list_odd = []
    [list_even.append(i) for i in lst if i%2==0]
    [list_odd.append(i) for i in lst if i%2!=0]
    even_count = len(list_even)
    odd_count = len(list_odd)
    return even_count, odd_count

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_count, odd_count = count_even_odd(lst)
    print(f"Even count: {even_count}, Odd count: {odd_count}")