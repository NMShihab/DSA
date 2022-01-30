def binary_search(target, input_list):
    start = 0
    last = len(input_list) - 1

    while start <= last:
        midpoint = (start + last) // 2

        if input_list[midpoint] == target:
            return midpoint
        elif input_list[midpoint] > target:
            last = midpoint - 1
        else:
            start = midpoint + 1

    return None


sorted_list = [1, 2, 4, 5, 7, 8, 12, 14, 15, 25, 28, 30]
index_of_search = binary_search(25, sorted_list)
print(index_of_search)
