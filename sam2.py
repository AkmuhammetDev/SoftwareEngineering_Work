def remove_tuple_element(tuple_data, element):
    lst = list(tuple_data)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

print(remove_tuple_element((1, 2, 3), 1))
print(remove_tuple_element((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_tuple_element((2, 4, 6, 6, 4, 2), 9))