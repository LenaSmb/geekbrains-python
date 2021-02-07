class ZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text
    
a = int(input('Введите 1-е число >>> '))
b = int(input('Введите 2-ое число >>> '))
    
try:
    if b == 0:
        raise ZeroDivisionError('деление на ноль')
except ZeroDivisionError:
    print('На ноль делить нельзя')
else:
   print(a / b)