from random import choice


def compare_characters():
    first = 'Мама мыла раму'
    second = 'Рамена мало было'


    result = list(map(lambda a, b: a == b, first, second))

    print("Сравнение символов двух строк по позициям:")
    print(result)
    print()


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything



class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


if __name__ == "__main__":
    compare_characters()

    writer = get_advanced_writer('example.txt')
    writer('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    print("Данные записаны в файл 'example.txt'.")
    print()


    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print("Результаты MysticBall:")
    print(first_ball())
    print(first_ball())
    print(first_ball())

