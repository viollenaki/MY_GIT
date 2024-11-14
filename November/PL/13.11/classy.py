class Clients:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.balance = 0
    
    def remove(self, amount):
        self.balance -= amount
    
    def add(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance
    
    def get_Name(self):
        return self.name


class Optima:
    def __init__(self):
        self.clients_id = {}
        self.total = 0
        self.history = []
        self.profit = 0

    def addClient(self):
        name = input("Enter client name: ")
        id = int(input("Enter client ID: "))
        self.clients_id[id] = Clients(name, id)
        self.history.append(f'Client {name} added with id {id}')
        print(f'Client {name} added with id {id}')
    
    def addBalance(self):
        id = int(input("Enter client ID: "))
        if id in self.clients_id:
            amount = int(input("Enter amount to add: "))
            self.clients_id[id].add(amount)
            self.total += amount
            self.history.append(f'Balance of {id} added with amount {amount}')
            print(f'Balance of {id} added with amount {amount}')
        else:
            print(f'Client with id {id} not found')

    def transfer(self):
        from_id = int(input("Enter sender client ID: "))
        to_id = int(input("Enter receiver client ID: "))
        if from_id in self.clients_id and to_id in self.clients_id:
            amount = int(input("Enter amount to transfer: "))
            komissiya = amount * 0.1 / 100
            if self.clients_id[from_id].get_balance() >= (amount + komissiya):
                self.clients_id[to_id].add(amount)
                self.clients_id[from_id].remove(amount + komissiya)
                self.profit += komissiya
                self.history.append(f'Transfer {amount} from {from_id} to {to_id}')
                print(f'Transfer {amount} from {from_id} to {to_id} (commission: {komissiya})')
            else:
                print(f'Insufficient balance for transfer from {from_id}')
        else:
            print(f'Client not found for ID {from_id} or {to_id}')
    
    def getBalance(self):
        id = int(input("Enter client ID to get balance: "))
        if id in self.clients_id:
            print(f'Balance of {id}: {self.clients_id[id].get_balance()}')
        else:
            print(f'Client with id {id} not found')
    
    def getProfit(self):
        print(f'Profit: {self.profit}')
    
    def showHistory(self):
        print("History:")
        for entry in self.history:
            print(entry)


