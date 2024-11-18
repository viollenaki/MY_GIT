class Flight:
    def _init_(self, flight_number, destination, departure_time, total_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passengers = []

    def sell_ticket(self, passenger_name):
        if self.available_seats > 0:
            self.passengers.append(passenger_name)
            self.available_seats -= 1
            return True
        else:
            return False

    def return_ticket(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            self.available_seats += 1

    def get_flight_info(self):
        return (f'Flight: {self.flight_number}\n'
                f'Destination: {self.destination}\n'
                f'Departure: {self.departure_time}\n'
                f'Available Seats: {self.available_seats}/{self.total_seats}\n')


class Passenger:
    def _init_(self, name):
        self.name = name
        self.tickets = []


class Airline:
    def _init_(self):
        self.flights = {}
        self.passengers = {}
        self.history = []

    def add_flight(self, flight_number, destination, departure_time, total_seats):
        print(f'Flight {flight_number} to {destination} is being added.\n')
        self.flights[flight_number] = Flight(flight_number, destination, departure_time, total_seats)
        self.history.append(f'Flight {flight_number} added.')

    def sell_ticket(self, flight_number, passenger_name):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            if flight.sell_ticket(passenger_name):
                if passenger_name not in self.passengers:
                    self.passengers[passenger_name] = Passenger(passenger_name)
                self.passengers[passenger_name].tickets.append(flight_number)
                self.history.append(f'{passenger_name} bought a ticket for flight {flight_number}.')
            else:
                print(f'No available seats on flight {flight_number}.\n')
        else:
            print(f'Flight {flight_number} does not exist.\n')

    def return_ticket(self, flight_number, passenger_name):
        if flight_number in self.flights and passenger_name in self.passengers:
            flight = self.flights[flight_number]
            flight.return_ticket(passenger_name)
            self.passengers[passenger_name].tickets.remove(flight_number)
            self.history.append(f'{passenger_name} returned a ticket for flight {flight_number}.\n')

    def get_available_flights(self):
        print('----AVAILABLE FLIGHTS----')
        for flight_number, flight in self.flights.items():
            if flight.available_seats > 0:
                print(flight.get_flight_info())

    def get_sold_out_flights(self):
        print('----SOLD OUT FLIGHTS----')
        for flight_number, flight in self.flights.items():
            if flight.available_seats == 0:
                print(flight.get_flight_info())

    def get_history(self):
        print('----TRANSACTION HISTORY----')
        for entry in self.history:
            print(entry)

    def get_passenger_tickets(self, passenger_name):
        if passenger_name in self.passengers:
            print(f'Flights for {passenger_name}:')
            for flight_number in self.passengers[passenger_name].tickets:
                print(flight_number)


# Пример использования
airline = Airline()

# Добавляем рейсы
airline.add_flight('KG101', 'Bishkek', '18-11-2024 14:30', 100)
airline.add_flight('KG202', 'Osh', '19-11-2024 09:00', 50)

# Просмотр доступных рейсов
airline.get_available_flights()

# Продажа билетов
airline.sell_ticket('KG101', 'Akbar')
airline.sell_ticket('KG101', 'Atabek')

# Возврат билета
airline.return_ticket('KG101', 'Akbar')

# Просмотр рейсов, где нет мест
airline.get_sold_out_flights()

# История транзакций
airline.get_history()

# Билеты, купленные пассажиром
airline.get_passenger_tickets('Atabek')                                 