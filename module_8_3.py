class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number: int) -> int:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __is_valid_numbers(self, numbers: str) -> str:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера, должна содержать 6 символов')
        return numbers

    def get_vin(self) -> int:
        return self.__vin

    def get_numbers(self) -> str:
        return self.__numbers

    def __str__(self) -> str:
        return f'Car(model={self.model}, vin={self.__vin}, numbers={self.__numbers})'

# Основной код для создания объектов Car
def main():
    car_data = [
        ('Model1', 1000000, 'f123dj'),
        ('Model2', 300, 'т001тр'),  # Это вызовет исключение
        ('Model3', 2020202, 'нет номера')  # Это также вызовет исключение
    ]

    for model, vin, numbers in car_data:
        try:
            car = Car(model, vin, numbers)
            print(car)  # Вывод успешного создания автомобиля
        except (IncorrectVinNumber, IncorrectCarNumbers) as e:
            print(f"Ошибка при создании {model}: {e}")

if __name__ == "__main__":
    main()
