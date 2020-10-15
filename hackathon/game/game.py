import hackathon


class Game:
    def __init__(self, robots: list, *args, **kwargs):  # robots is list of str
        self.env = hackathon.container.Environment()
        self.robots = robots

    def run(self, *args, **kwargs):
        pass
