def find_second_smallest(my_list):
    if len(my_list) < 1:
        return None

    smallest = my_list[0]
    second_smallest = smallest

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return second_smallest

print(find_second_smallest([1, 2, 0, -1]))
