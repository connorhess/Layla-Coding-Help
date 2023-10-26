def adding_up_to(lst, index):
    if index == 0:
        return lst[0]
    else:
        return lst[index] + adding_up_to(lst, index-1)

print(adding_up_to([1,4,5,3,12,16], 4))