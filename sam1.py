user_input = input()
numbers_list = user_input.split()
final_list = []
for num_str in numbers_list:
    final_list.append(int(num_str))
final_tuple = tuple(final_list)
print(final_list)
print(final_tuple)