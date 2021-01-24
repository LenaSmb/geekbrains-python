class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)

    def show_speed(self):
        print(self.name, self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(self.name, self.speed, 'speed limit exceeded')
        else:
            print(self.name, self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(self.name, self.speed, 'speed limit exceeded')
        else:
            print(self.name, self.speed)


class PoliceCar(Car):
    pass

car = Car(100, 'black', 'aston martin', False)
car.go()
car.turn('left')
car.show_speed()
car.stop()

car = TownCar(120, 'red', 'ford', False)
car.go()
car.turn('right')
car.show_speed()
car.stop()

car = WorkCar(220, 'green', 'bmw', False)
car.go()
car.turn('right')
car.show_speed()
car.stop()

car = PoliceCar(30, 'white', 'renault', True)
car.go()
car.turn('right')
car.show_speed()
car.stop()
