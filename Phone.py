class Phone:

    def __init__(self, number, model, weight=None):
        self.number = number
        self.model = model
        self.weight = weight

    def recieveCall(self, name=None):
        if name is None:
           print(f'{self.number}')
        else:
            print(f'{name}, {self.number}')

    def getNumber(self):
        return self.number

    def sendMessage(self, *args):
        print(args)

    def __repr__(self):
        return f'Number: {self.number}, Model: {self.model}, Weight: {self.weight}'

a = Phone(9130445265, 'Samsung')
b = Phone(9082456589, 'iPhone')
c = Phone(9088745652, 'Honor', 120)

print(a)
print(b)
print(c)

print(a.recieveCall('Alex'))
print(b.recieveCall('Norman'))
print(c.recieveCall())


print(a.getNumber())
print(b.getNumber())
print(c.getNumber())
print(a.sendMessage(9123214112, 1233214123, 912314142))
print(b.sendMessage(9123214112, 1233214123, 912314142))
print(c.sendMessage(9126546235, 9856354125, 912545484))