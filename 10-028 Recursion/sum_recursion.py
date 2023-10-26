import ast

def adding_up_to(lst, index):
    if index == 0:
        return lst[0]
    else:
        return lst[index] + adding_up_to(lst, index-1)



lst_str = input("Enter a list of numbers: ")
lst = ast.literal_eval(lst_str)

index_str = input("Enter an index: ")
index = int(index_str)

result = adding_up_to(lst, index)
print(result)
