import constants as c

from Classes.Car import Car


class MyCar(Car):

    def __init__(self) -> None:
        self.image: str = 'MyDreamCar/img/car7.png'
        self.x: int = c.CAR_STARTING_X
        self.y: int = c.CAR_STARTING_Y
        super(MyCar, self).__init__()
