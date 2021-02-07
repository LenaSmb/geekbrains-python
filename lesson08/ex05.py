class Warehouse:
    equipment = {}
    quantity = {}
    transfered = {}

    def __init__(self):
        pass

    def status(self):
        for key in self.equipment.keys():
            print(key, self.quantity[key], end='; ')
        
        print()

    def receive(self, item):
        if item.name not in self.equipment.keys():
            self.equipment[item.name] = {}
            self.quantity[item.name] = 0
        
        self.equipment[item.name][item.inventoryNumber] = item
        self.quantity[item.name] += 1
            
    def transfer(self, equipment_type, quantity, unit):
        if equipment_type not in self.equipment.keys():
            raise ValueError('no such item with given inventory number')
        
        if quantity > self.quantity[equipment_type]:
            raise ValueError('no such quantity of given equipment')

        if unit not in self.transfered.keys():
            self.transfered[unit] = []

        for _ in range(0, quantity):
            item = self.equipment[equipment_type].popitem()

            self.transfered[unit].append(item)
            self.quantity[equipment_type] -= 1


class Equipment:
    inventoryNumber: int

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def __init__(self, inventoryNumber):
        self.inventoryNumber = inventoryNumber


class Printer(Equipment):
    technology: str
    
    def __init__(self, inventoryNumber, technology):
        super().__init__(inventoryNumber)
        self.technology = technology

class Scanner(Equipment):
    resolution: int
    
    def __init__(self, inventoryNumber, resolution):
        super().__init__(inventoryNumber)
        self.resolution = resolution

class Xerox(Equipment):
    resize: bool

    def __init__(self, inventoryNumber, resize):
        super().__init__(inventoryNumber)
        self.resize = resize

printer = Printer(2, 'laser')
print(printer.name)

warehouse = Warehouse()
warehouse.receive(Printer(1, 'laser'))
warehouse.receive(Scanner(2, 8000))
warehouse.receive(Xerox(3, True))

warehouse.status()

warehouse.transfer('printer', 1, 'accounting')

warehouse.status()