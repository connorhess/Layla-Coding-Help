def largest_number(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_num = largest_number(lst[1:])
        return max_num if max_num > lst[0] else lst[0]

print(largest_number([1]))
print(largest_number([3, 6, 4, 5]))
print(largest_number([10, 20, 30, 40, 50]))
