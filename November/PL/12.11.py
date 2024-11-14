# Эта программа откроет файл с именем 'grades.csv' и прочитает его. После этого
# она создаст экземпляр класса Akbar с данными из файла.
# Класс Akbar имеет методы для вывода данных, получения максимального и
# минимального значений и среднего значения в файле.

from csv import reader
with open(r'C:\Users\User\Desktop\GIT AIT Akbar\November\grades.csv', 'r', encoding='utf-8') as fil:
    fil = list(reader(fil))

class Akbar:
    def __init__(self, fil) -> None:
        # header — это первая строка файла, содержащая заголовки столбцов
        self.header = fil[0]
        # fil — это список всех строк в файле
        self.fil = fil[1:]

    def prin(self):
        # этот метод выводит все строки в файле
        for i in self.fil:
            print(i)
        return

    def get_max(self):
        # этот метод возвращает строку с максимальным значением балла
        return max([(int(score), name) for name, score in self.fil])

    def get_min(self):
        # этот метод возвращает строку с минимальным значением балла
        return min([(int(score), name) for name, score in self.fil])

    def get_average(self):
        # этот метод возвращает среднее значение балла всех строк в файле
        # если файл пустой, он возвращает 0
        total_score = sum(int(score) for name, score in self.fil)
        return total_score / len(self.fil) if self.fil else 0
    
arbuz = Akbar(fil)

print(arbuz.get_max())
print(arbuz.get_min())





















