from datetime import datetime, timedelta, date
import calendar

class Barber:
    def __init__(self, name, price, start, end):
        self.name = name
        self.price = price
        self.start = datetime.strptime(start, '%H:%M').time()
        self.end = datetime.strptime(end, '%H:%M').time()
        self.total = 0
        self.reservations = []

    def add_money(self, amount):
        self.total += amount

    def add_reservation(self, date, time, client_name):
        reservation_time = datetime.strptime(time, '%H:%M').time()
        if self.start <= reservation_time <= self.end:
            self.reservations.append((date, time, client_name))
            print(f"Reservation for {client_name} on {date} at {time} with {self.name} is confirmed.")
        else:
            print(f"{time} is outside the working hours for {self.name}.")

    def is_day_reserved(self, day):
        # Проверяет, есть ли бронирования на указанный день
        return any(reservation[0] == day for reservation in self.reservations)


class Barbershop:
    def __init__(self):
        self.barbers = {}
        self.kassa = 0  # Добавляем кассу
        self.history = []

    def add_barber(self, name, price, start, end):
        if name in self.barbers:
            print(f"Barber {name} already exists.")
        else:
            self.barbers[name] = Barber(name, price, start, end)
            print(f"Barber {name} added with working hours {start}-{end}.")

    def remove_master(self, name):
        if name in self.barbers:
            del self.barbers[name]
            print(f"Barber {name} removed.")
        else:
            print(f"Barber {name} not found.")

    def reserve(self, client_name, barber_name, date, time):
        if barber_name in self.barbers:
            barber = self.barbers[barber_name]
            barber.add_reservation(date, time, client_name)
            barber.add_money(barber.price)
            self.kassa += barber.price  # Добавляем стоимость бронирования в кассу
            self.history.append((client_name, barber_name, date, time))
        else:
            print(f"Barber {barber_name} not found.")

    def reserve_recurring_weekly(self, client_name, barber_name, time, weekday, start_date, end_date):
        if barber_name not in self.barbers:
            print(f"Barber {barber_name} does not exist.")
            return
        
        current_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        
        while current_date <= end_date:
            if current_date.weekday() == weekday:
                self.reserve(client_name, barber_name, current_date.strftime('%d-%m-%Y'), time)
            current_date += timedelta(days=1)

    def reserve_recurring_monthly(self, client_name, barber_name, time, day_of_month, start_date, end_date):
        if barber_name not in self.barbers:
            print(f"Barber {barber_name} does not exist.")
            return
        
        current_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        
        while current_date <= end_date:
            if current_date.day == day_of_month:
                self.reserve(client_name, barber_name, current_date.strftime('%d-%m-%Y'), time)
            next_month = current_date.replace(day=28) + timedelta(days=4)  # Переход к следующему месяцу
            current_date = next_month.replace(day=day_of_month)

    def get_kassa(self):
        # Выводит текущую кассу (суммарный доход)
        print(f"Total income (kassa): {self.kassa}")
        return self.kassa

    def get_history(self):
        return self.history
    
    def get_all_barbers(self):
        for names in self.barbers.keys():
            print(names)

    def get_free_days_of_barber(self, barber_name, year, month):
        if barber_name not in self.barbers:
            print(f"Barber {barber_name} does not exist.")
            return
        
        barber = self.barbers[barber_name]
        cal = calendar.monthcalendar(year, month)
        print(f"Free days for {barber_name} in {calendar.month_name[month]} {year}:")
        
        for week in cal:
            for day in week:
                if day == 0:
                    print("  ", end=" ")  # Пустой день (дни вне месяца)
                else:
                    day_str = f"{day:02d}-{month:02d}-{year}"
                    if barber.is_day_reserved(day_str):
                        print("X", end=" ")
                    else:
                        print(day, end=" ")
            print()  # Новый ряд

    def get_client_history(self, client_name):
        print(f"History for {client_name}:")
        found = False
        for record in self.history:
            if record[0] == client_name:
                print(f"Client: {record[0]}, Barber: {record[1]}, Date: {record[2]}, Time: {record[3]}")
                found = True
        if not found:
            print(f"No history found for {client_name}.")

def main():
    barbershop = Barbershop()

    while True:
        print("\n1. Add Barber")
        print("2. Remove Barber")
        print('3. Reserve Appointment or Recurring')
        print("4. View History")
        print("5. View Kassa")
        print('6. Get all barbers')
        print("7. Get free days of Barber")
        print("8. Get Client History")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            name = input("Enter barber name: ")
            price = float(input("Enter price: "))
            start = input("Enter start time (HH:MM): ")
            end = input("Enter end time (HH:MM): ")
            barbershop.add_barber(name, price, start, end)

        elif choice == '2':
            name = input("Enter barber name to remove: ")
            barbershop.remove_master(name)

        elif choice == '3':
            print('Choose your reserve type')
            print("1. Reserve Appointment")
            print("2. Reserve Recurring Weekly")
            print("3. Reserve Recurring Monthly")
            choice = input('Your choice: ')
            if choice == '1':
                client_name = input("Enter client name: ")
                barber_name = input("Enter barber name: ")
                date = input("Enter date (dd-mm-yyyy): ")
                time = input("Enter time (HH:MM): ")
                barbershop.reserve(client_name, barber_name, date, time)

            elif choice == '2':
                client_name = input("Enter client name: ")
                barber_name = input("Enter barber name: ")
                time = input("Enter time (HH:MM): ")
                weekday = int(input("Enter weekday (0=Monday, 6=Sunday): "))
                start_date = input("Enter start date (dd-mm-yyyy): ")
                end_date = input("Enter end date (dd-mm-yyyy): ")
                barbershop.reserve_recurring_weekly(client_name, barber_name, time, weekday, start_date, end_date)

            elif choice == '3':
                client_name = input("Enter client name: ")
                barber_name = input("Enter barber name: ")
                time = input("Enter time (HH:MM): ")
                day_of_month = int(input("Enter day of the month (1-31): "))
                start_date = input("Enter start date (dd-mm-yyyy): ")
                end_date = input("Enter end date (dd-mm-yyyy): ")
                barbershop.reserve_recurring_monthly(client_name, barber_name, time, day_of_month, start_date, end_date)

        elif choice == '4':
            history = barbershop.get_history()
            for record in history:
                print(f"Client: {record[0]}, Barber: {record[1]}, Date: {record[2]}, Time: {record[3]}")

        elif choice == '5':
            barbershop.get_kassa()

        elif choice == '6':
            barbershop.get_all_barbers()

        elif choice == '7':
            barber_name = input("Enter barber name: ")
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            barbershop.get_free_days_of_barber(barber_name, year, month)

        elif choice == '8':
            client_name = input("Enter client name: ")
            barbershop.get_client_history(client_name)

        elif choice == '0':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
