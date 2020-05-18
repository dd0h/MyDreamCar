from Classes import Obstacle

class ObstacleGenerator:

    def __init__(self, score):
        self.score = score

    def generate(self):
        return Obstacle.Obstacle()
