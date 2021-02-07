class Date:
    day: int
    month: int
    year: int

    def __init__(self, date):
        day, month, year = self.extract(date)
        
        if self.validate(day, month, year):
            self.day = day
            self.month = month
            self.year = year
        else:
            raise ValueError('Incorrect input date')

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'

    @staticmethod
    def validate(day, month, year):
        correct = 1 <= day <= 31 and 1 <= month <= 12
        positive = day > 0 and month > 0 and year > 0

        return correct and positive

    @classmethod
    def extract(cls, date):
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

d = Date('31-12-2020')
print(d)

d = Date('32-12-2020')
print(d)