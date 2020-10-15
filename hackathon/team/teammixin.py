from hackathon.team import Team


class TeamMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.teams = [Team(name=code[42:69], code=code) for code in kwargs["robots"]]
