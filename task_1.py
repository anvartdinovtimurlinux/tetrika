# Дан массив целых чисел array и целое число k.
# Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.
# Примечание: под уникальностью понимается следующее:
# если ответу удовлетворяет несколько пар вида (a, b) и (b, a),
# то достаточно вывести только одну пару (a, b).

# def search_pairs(array, k):
# """Cложность алгоритма O(n^2)"""
#     result = set()
#     for i, el_1 in enumerate(array[:-1]):
#         for el_2 in array[i + 1:]:
#             if el_1 + el_2 == k:
#                 result.add((
#                     min(el_1, el_2),
#                     max(el_1, el_2)
#                 ))
#     return list(result)


def search_pairs(array, k):
    """Сложность алгоритма O(n)"""
    result = set()
    pairs = {}

    for i in array:
        if pairs.get(i):
            result.add((i, k - i))
        else:
            pairs[k - i] = i

    return list(result)


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2, 3], 5))
print(search_pairs([1, 2, 3, 4, 5, 6, -2, -1, 0, 2], 5))
