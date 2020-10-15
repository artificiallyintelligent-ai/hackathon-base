# designed to be a list of robots
class Team(list):
    def __init__(self, *args, name="", code="", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.code = code
