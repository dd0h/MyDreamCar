import constants as c

from Classes.Car import Car


class MyCar(Car):

    def __init__(self):
        self.image = 'MyDreamCar/img/car7.png'
        self.x = c.CAR_STARTING_X
        self.y = c.CAR_STARTING_Y
        super(MyCar, self).__init__()
