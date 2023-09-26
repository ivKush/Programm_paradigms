# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array

# В декларативном стиле

def sort_list_declarative(array):
    array.sort(reverse=True)
    return array

print(sort_list_imperative([5, 1, 2, 8, 6, 7, 10, 15, 20, 0]))

print(sort_list_declarative([5, 1, 2, 8, 6, 7, 10, 15, 20, 0]))