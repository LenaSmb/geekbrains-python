class Warehouse:
    pass

class Equipment:
    inventoryNumber: int
    brand: str


class Printer(Equipment):
    technology: str
    
    def __init__(self, inventoryNumber, technology):
        self.inventoryNumber = inventoryNumber
        self.technology = technology

class Scanner(Equipment):
    resolution: int
    
    def __init__(self, inventoryNumber, resolution):
        self.inventoryNumber = inventoryNumber
        self.resolution = resolution

class Xerox(Equipment):
    resize: bool

    def __init__(self, inventoryNumber, resize):
        self.inventoryNumber = inventoryNumber
        self.resize = resize

printer = Printer(1, 'laser')
scanner = Scanner(2, 8000)
xerox = Xerox(3, True)
