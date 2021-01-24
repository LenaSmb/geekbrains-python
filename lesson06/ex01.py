import time
from collections import OrderedDict


class TrafficLight:
    _color = None
    _colors = OrderedDict({
        'red' : 7,
        'yellow' : 2,
        'green' : 7
    })

    def running(self):
        while True:
            for color, duration in self._colors.items():
                print(color)
                time.sleep(duration)

traffic = TrafficLight()
traffic.running()
