def merge_sort(items):
    """
    Sorts a list of items using the merge sort algorithm.
    
    Args:
        items (list): The list of items to be sorted.
        
    Returns:
        list: A new sorted list containing all items from the input.
    """
    # Step 1: Split the input list into a list of single-item lists
    items_list = split(items)
    
    # Step 2: Repeatedly merge adjacent pairs of lists until only one list remains
    while len(items_list) != 1:
        index = 0
        # Go through the list, merging pairs of lists
        while index < len(items_list) - 1:
            # Merge the current list and the next list
            new_list = merge(items_list[index], items_list[index + 1])
            # Replace the current list with the merged list
            items_list[index] = new_list
            # Remove the next list, as it has been merged
            del items_list[index + 1]
            # Move to the next pair
            index += 1
    # Only one sorted list remains, return it
    return items_list[0]

def split(items):
    """
    Splits a list into a list of single-item lists.
    
    Args:
        items (list): The list to split.
        
    Returns:
        list: A list where each element is a single-item list from the original list.
    """
    list_of_items = []
    # For each item in the input list, create a new list containing just that item
    for n in range(len(items)):
        item = [items[n]]
        list_of_items.append(item)
    return list_of_items

def merge(list1, list2):
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.
        
    Returns:
        list: A new sorted list containing all elements from both input lists.
    """
    new_list = []  # This will store the merged, sorted items
    index1 = 0     # Pointer for list1
    index2 = 0     # Pointer for list2
    # Compare elements from both lists and add the smaller one to new_list
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            new_list.append(list1[index1])
            index1 += 1
        elif list1[index1] > list2[index2]:
            new_list.append(list2[index2])
            index2 += 1
        else:  # If elements are equal, add both
            new_list.append(list1[index1])
            new_list.append(list2[index2])
            index1 += 1
            index2 += 1
    # If there are any remaining elements in list1, add them to new_list
    while index1 < len(list1):
        new_list.append(list1[index1])
        index1 += 1
    # If there are any remaining elements in list2, add them to new_list
    while index2 < len(list2):
        new_list.append(list2[index2])
        index2 += 1
    return new_list

# Example usage
items = ["Florida", "Georgia", "Delaware", "Alabama", "California"]
# Print the sorted list
print(merge_sort(items))


