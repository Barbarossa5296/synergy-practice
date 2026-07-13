class DataProcessor:
    def __init__(self, data: list[int]) -> None:
        self.data = data

    @property
    def data(self) -> list[int]:
        return self.__data.copy()

    @data.setter
    def data(self, value: list[int]) -> None:
        if not value:
            raise ValueError("Список данных не должен быть пустым.")

        self.__data = value.copy()

    def show_data(self) -> None:
        print(f"Данные: {self.__data}")

    def process(self) -> None:
        print(f"Количество элементов: {len(self.__data)}")


class NumberProcessor(DataProcessor):
    def process(self) -> None:
        data = self.data
        total = sum(data)
        average = total / len(data)

        print(f"Сумма элементов: {total}")
        print(f"Среднее значение: {average}")

    def find_min_max(self) -> None:
        data = self.data

        print(f"Минимальный элемент: {min(data)}")
        print(f"Максимальный элемент: {max(data)}")


def main() -> None:
    try:
        base_processor = DataProcessor([10, 20, 30])
        number_processor = NumberProcessor([5, -2, 8, 4])

        processors: list[DataProcessor] = [
            base_processor,
            number_processor,
        ]

        for processor in processors:
            print(f"\nКласс: {processor.__class__.__name__}")
            processor.show_data()
            processor.process()

        print("\nСобственный метод производного класса:")
        number_processor.find_min_max()

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()