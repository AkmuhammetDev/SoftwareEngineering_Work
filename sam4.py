def get_office_entries(tuple_data, element):
    if element not in tuple_data:
        return ()

    first_index = tuple_data.index(element)

    if tuple_data.count(element) == 1:
        return tuple_data[first_index:]

    second_index = tuple_data.index(element, first_index + 1)
    return tuple_data[first_index:second_index + 1]


print(get_office_entries((1, 2, 3), 8))
print(get_office_entries((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_office_entries((1, 2, 8, 5, 1, 2, 9), 8))