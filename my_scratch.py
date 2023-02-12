def compute_sort(lst):
    new_list = lst[:]
    new_list.sort()

    return new_list


x = [5,2,3,4,1]

print(x)
print(compute_sort(x))
print(x)