from hackathon import Environment
from hackathon import Map


class Game:
    def __init__(self, robots: list, *args, **kwargs):
        self.env = Environment()
        self.robots = robots

        self.map = Map()

    def run(self, *args, **kwargs):
        pass
