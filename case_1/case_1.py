def sum_negative_between_min_max(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Массив не должен быть пустым.")

    max_value = max(arr)
    min_value = min(arr)

    max_ind = arr.index(max_value)
    min_ind = arr.index(min_value)

    left_ind = min(min_ind, max_ind) + 1
    right_ind = max(min_ind, max_ind)

    total = 0

    for ind in range(left_ind, right_ind):
        if arr[ind] < 0:
            total += arr[ind]

    return total


def main() -> None:
    try:
        n = int(input("Введите количество элементов массива N: "))

        if n <= 0:
            raise ValueError(
                "Размер массива должен быть положительным числом."
            )

        arr = list(
            map(
                int,
                input(
                    f"Введите {n} целых чисел через пробел: "
                ).split(),
            )
        )

        if len(arr) != n:
            raise ValueError(
                f"Указано N = {n}, но введено элементов: {len(arr)}."
            )

        result = sum_negative_between_min_max(arr)

        print(f"Исходный массив: {arr}")
        print(f"Максимальный элемент: {max(arr)}")
        print(f"Минимальный элемент: {min(arr)}")
        print(
            "Сумма отрицательных элементов между "
            f"максимальным и минимальным элементами: {result}"
        )

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()