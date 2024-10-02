def generate_lists(lst):
    result = []
    for i in range(len(lst)):
        new_list = lst[:i] + lst[i+1:]
        result.append(new_list)
    return result

# Example usage
lst = [2, 3, 3, 2, 4]
output_lists = generate_lists(lst)

for l in output_lists:
    print(l)