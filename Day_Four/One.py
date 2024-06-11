def second_largest(lst):
    if len(lst) < 2:
        return "List must have at least two elements"
    
    # Sorting the list in descending order
    sorted_lst = sorted(lst, reverse=True)
    
    return sorted_lst[1]

# Example usage:
my_list = [10, 20, 30, 40, 50]
print("Second largest number:", second_largest(my_list))
