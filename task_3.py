# Факториал числа n равен произведению всех чисел от 1 до n, то есть:
# n! = 1 * 2 * 3 * ... * n
# Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.
# def get_zeros(n):
# ....
# print(get_zeros(5))
# OUT: >> 1
# print(get_zeros(12))
# OUT: >> 2


def get_zeros(n):
    def get_five_degree(number):
        degree = 0
        while True:
            if number // 5 == number / 5:
                degree += 1
            else:
                break
            number //= 5
        return degree

    zero_count = 0
    for i in range(1, n + 1):
        zero_count += get_five_degree(i)

    return zero_count


print(get_zeros(5))  # 1
print(get_zeros(12))  # 2
print(get_zeros(50))  # 12
# Сложность алгоритма O(n*log(n))
