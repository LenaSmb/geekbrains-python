class Matrix:
    values = []

    def __init__(self, values: list):
        self.values = values

    def __str__(self):
        output = ''

        for row in self.values:
            for value in row:
                output = output + str(value) + '  '
            
            output += '\n'

        return output

    def __add__(self, other):
        result = []

        for i, row in enumerate(self.values):
            result_row = []

            for j, value in enumerate(row):
                result_row.append(value + other.values[i][j])
            
            result.append(result_row)

        return Matrix(result)
            
a = Matrix([[2, -3, 0], [4, 5, 6]])
b = Matrix([[3, 3, -1], [-2, -5, 4]])

print(a)

c = a + b

print(c)
