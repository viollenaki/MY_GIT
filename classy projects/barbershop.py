class Client:
    def __init__(self, name):
        self.name = name
        self.history = []

    def add_hairstyle(self, hairstyle):
        self.history.append(hairstyle)
        return self  # Return the instance to allow method chaining

    def get_history(self):
        for entry in self.history:
            print(entry)

    def get_popular_hairstyle(self):
        dict = {}
        for entry in self.history:
            dict[entry] = dict.get(entry, 0) + 1
        if dict:  # Check if the dictionary is not empty
            print(max([(count, name) for name, count in dict.items()]))
        else:
            print("No hairstyles in history")


class Barbershop:
    def __init__(self):
        self.clients = {}
        self.history = []
        self.total = 0
        self.hairstyle_cost = {
            'mohawk': 100,
            'bald': 50,
            'pixie': 75,
            'bob': 150,
            'crew': 200,
            'braid': 250,
            'mullet': 300
        }


    def serve_client(self, client, hairstyle):
        if client not in self.clients:
            self.clients[client] = Client(client)
        self.clients[client].add_hairstyle(hairstyle)
        self.total += self.hairstyle_cost[hairstyle]
        self.history.append((client, hairstyle))

    def get_history(self):
        for client, hairstyle in self.history:
            print(f'{client} got {hairstyle}')

    def get_most_popular(self):
        dict = {}
        for client, hairstyle in self.history:
            dict[hairstyle] = dict.get(hairstyle, 0) + 1
        if dict:  
            print(max([(count, hairstyle) for hairstyle, count in dict.items()]))
        else:
            print("No hairstyles in history")

    def get_most_popular_client(self):
        dict = {}
        for client, _ in self.history:
            dict[client] = dict.get(client, 0) + 1
        if dict:
            print(max([(count, client) for client, count in dict.items()]))
        else:
            print("No clients in history")

    def get_client_most_popular_hairstyle(self, client):
        if client not in self.clients:
            return 'Client not found'
        else:
            self.clients[client].get_popular_hairstyle()

    def get_total(self):
        return self.total


italiabarber = Barbershop()
italiabarber.serve_client('John', 'mohawk')
italiabarber.serve_client('Jane', 'bald')
italiabarber.serve_client('Bob', 'pixie')
italiabarber.serve_client('Alice', 'bob')
italiabarber.serve_client('Charlie', 'crew')
italiabarber.serve_client('David', 'braid')
italiabarber.serve_client('John', 'mohawk')
italiabarber.serve_client('John', 'mohawk')
italiabarber.serve_client('Alice', 'mohawk')
italiabarber.serve_client('David', 'mohawk')

italiabarber.get_history()
italiabarber.get_most_popular()
italiabarber.get_most_popular_client()
italiabarber.get_client_most_popular_hairstyle('John')


italiabarber.get_total()