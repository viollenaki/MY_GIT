from datetime import datetime

class Place:
    def __init__(self, id):
        self.id = id
        self.available = True
        self.history = []

    def enter(self, name, entry_datetime):
        """
        Метод для въезда на парковку.
        entry_datetime — это строка формата '%d-%m-%Y %H:%M:%S', например, '18-11-2024 14:30:00'.
        """
        if self.available:
            self.available = False
            self.history.append({
                'id': self.id, 
                'entry_date': entry_datetime, 
                'name': name
            })

    def exit(self, exit_datetime, time_stayed):
        """
        Метод для выезда с парковки.
        exit_datetime — это строка формата '%d-%m-%Y %H:%M:%S', например, '18-11-2024 16:30:00'.
        time_stayed — время пребывания в минутах.
        """
        if not self.available:
            self.available = True
            last_entry = self.history[-1]
            if 'exit_date' not in last_entry:
                pay = (time_stayed / 60) * 20  # Оплата за час
                last_entry.update({
                    'exit_date': exit_datetime,
                    'time_stayed': time_stayed,
                    'pay': pay
                })

class Parking:
    def __init__(self):
        self.parking_data = {f'{i}{j}': Place(f'{i}{j}') for i in 'ABCDEFGHIJ' for j in range(1, 11)}

    def booking(self, id, name, entry_datetime):
        """
        Метод для бронирования парковочного места.
        id — это идентификатор места.
        name — имя человека.
        entry_datetime — время въезда.
        """
        if self.parking_data[id].available:
            self.parking_data[id].enter(name, entry_datetime)

    def exit(self, id, exit_datetime, time_stayed):
        """
        Метод для фиксации выезда с парковочного места.
        id — это идентификатор места.
        exit_datetime — время выезда.
        time_stayed — время пребывания в минутах.
        """
        if not self.parking_data[id].available:
            self.parking_data[id].exit(exit_datetime, time_stayed)

    def get_free_spaces(self):
        for space_id, place in self.parking_data.items():
            if place.available:
                print(space_id)

    def get_place_history(self, id):
        history = self.parking_data[id].history
        for i in range(len(history)):
            entry_record = history[i]
            exit_date = entry_record.get('exit_date', 'нет данных')
            pay = entry_record.get('pay', 'нет данных')
            print(f"Въезд: {entry_record['entry_date']}, {entry_record['name']}; Выезд: {exit_date}; Оплата: {pay}")

# Пример использования
asanbay = Parking()

# Въезд и выезд
asanbay.booking('A1', 'Atabek', '18-11-2024 14:30:00')
asanbay.exit('A1', '18-11-2024 16:30:00', 120)  # Пробыл 120 минут

asanbay.booking('A2', 'Akbar', '18-11-2024 15:00:00')
asanbay.exit('A2', '18-11-2024 15:45:00', 45)  # Пробыл 45 минут

# Просмотр истории
asanbay.get_place_history('A1')
asanbay.get_place_history('A2')