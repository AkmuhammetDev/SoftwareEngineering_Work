list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def create_set(numbers):
    result_set = set()
    for num in set(numbers):
        count = numbers.count(num)
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(num)
            else:
                result_set.add(str(num) * i)
    return result_set

print(create_set(list_1))
print(create_set(list_2))
print(create_set(list_3))