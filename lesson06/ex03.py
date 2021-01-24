class Worker:
    name = None
    surname = None
    position = None
    __income = {}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        
        self.__income = {
            'wage': wage,
            'bonus': bonus
        }

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_profit(self):
        return self.__income['wage'] + self.__income['bonus']

position = Position('John', 'Doe', 'manager', 1200, 500)

print(position.get_full_name())
print(position.get_full_profit())