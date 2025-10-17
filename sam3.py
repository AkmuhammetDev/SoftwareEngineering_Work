def count_numbers(text):
    count_dict = {}
    for char in text:
        num = int(char)
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    top_three = dict(sorted_items[:3])

    result = {}
    for key in sorted(top_three.keys()):
        result[key] = top_three[key]

    return result


text = input()
result_dict = count_numbers(text)
for key in sorted(result_dict.keys()):
    print(f"{key}: {result_dict[key]}")