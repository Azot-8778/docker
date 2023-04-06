# быстрая сортировка
# возвращает итоговую перестановку элементов массива A
# для того, чтобы можно было переставить элементы в любом другом массиве
def quick_argsort(A):
    import random

    # Алгоритм простой сортировки. Тут реализована пузырьковая сортировка
    def simple_sort(res, start, end):
        # Переменная. Нужна для цикла
        bit = False
        # Пока массив не упорядочен
        while not bit:
            # Проходим по массиву
            for i in range(start, end - 1):
                # Если текущий меньше предыдущего
                if res[i] > res[i + 1]:
                    # Меняем местами
                    res[i], res[i + 1] = res[i + 1], res[i]
            # Предварительно устанавливаем возможность выхода из цикла
            bit = True
            # Проходим по массиву
            for i in range(start, end - 1):
                # Если текущий меньше следующего, то
                if res[i] > res[i + 1]:
                    # То выходить из цикла рано.
                    bit = False
                    # Прерываем for
                    break

    # Lomuto's partition
    def partition(A, st, fn, number, pos):
        # Ставим ведущий элемент на последнее место
        A[pos], A[fn - 1] = A[fn - 1], A[pos]

        # Ставим индексы на начало указателя
        j = st
        i = st

        # Проходим по всему массиву
        for k in range(st, fn - 1):
            # Если текущий элемент больше ведущего
            if A[k] >= number:
                j += 1
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1

        # Устанавливаем ведущий элемент
        A[fn - 1], A[i] = A[i], A[fn - 1]

        return i

    # Функция для быстрой сортировки
    def quick_sort(A, st, fn):
        # Если размер массива больше 100
        if fn - st > 100:
            # то будем производить быструю сортировку
            # высчитываем случайным образом индек ведущего элемента
            pivot_index = random.randint(st, fn - 1)
            new_pos = partition(A, st, fn, A[pivot_index], pivot_index)
            quick_sort(A, st, new_pos)
            quick_sort(A, new_pos + 1, fn)
        else:
            # Иначе сделаем пузырьковую сортировку
            simple_sort(A, st, fn)

    # Вызываем функцию для быстрой сортировки
    quick_sort(A, 0, len(A))
    return A


A = [1, 23, 42, 2, -9, 8, 0]
quick_argsort(A)
print(A)
