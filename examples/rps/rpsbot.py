from examples.rps.team import RobotTeam
from hackathon import Robot


class RPSRobot(Robot):
    def __init__(self, game, code: str, side: RobotTeam):
        super().__init__(game, code)
        self.side = side

    def get_side(self):
        return self.side

    def get_turn(self):
        return len(self.game.actions)

    def get_action(self, turn: int, side: RobotTeam):
        return self.game.actions[turn][side]
