class Phone:

    def __init__(self, number, model, weight=150):
        self.number = number
        self.model = model
        self.weight = weight

    def recieveCall(self, name):
        return f'Звонит {name}'

    def getNumber(self):
        return self.number

    def __recieveCall__(self, name, number):
        return name, number

    def sendMessage(self, *args):
        return args

    def __repr__(self):
        return f'Number: {self.number}, Model: {self.model}, Weight: {self.weight}'

a = Phone(9130445265, 'Samsung')
b = Phone(9082456589, 'iPhone')
c = Phone(9088745652, 'Honor')

print(a)
print(b)
print(c)
print(a.sendMessage(9162254452, 874165416, 65464651321, 6454984564156,549848561651))
