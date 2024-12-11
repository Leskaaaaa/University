def find_max_elem_and_index():
    arr = (1, 3, 5, 4213, 43, 3654, 12, 2)
    max_elem = max(arr)
    index = arr.index(max_elem)

    print("Максимальный элемент: ", max_elem)
    print("Его индекс: ", index)

def get_sorted_odd_array():
    arr = (1, 3, 5, 4213, 43, 3654, 12, 2)
    odd_arr = []

    for num in arr:
        if num % 2 != 0:
            odd_arr.append(num)

    if odd_arr:
        odd_arr.sort(reverse=True)
        print("Массив нечетных чисел: ", odd_arr)
    else:
        print("Нечетных числе нет!")


find_max_elem_and_index()
get_sorted_odd_array()