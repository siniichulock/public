array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = int(input("Введите любое число: "))

while element > max(array) or element < min(array):
    print("Число не подходит. Попробуйте еще раз")
    element = int(input("Введите любое число: "))
else:
    array.append(element)


def poryadok(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] >= array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

poryadok(array)
index_element = binary_search(array, element, 0, len(array))-1
if array.count(element) > 1:
    index_element = index_element - (array.count(element)-1)


print(f"Индекс предыдущего числа: {index_element}" if index_element >= 0 else "Вы ввели наименьшее в последовательности число. Его индекс: 0")