class Road:
    _length = None
    _width = None
    _weight = 25
    _thickness = 0.05
  
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def weight(self):
        return self._length * self._width * self._weight * self._thickness

road = Road(5000, 20)
print(road.weight())