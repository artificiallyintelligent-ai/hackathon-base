from examples.rps.rpsbot import RPSRobot
from examples.rps.robotteam import RobotTeam
import hackathon

beat = {"R": "P", "P": "S", "S": "R"}
rbeat = {"P": "R", "S": "P", "R": "S"}


class RPSGame(hackathon.Game):
    def __init__(self, robots: list, *args, **kwargs):
        super().__init__(robots, *args, **kwargs)

        self.env.globals["RobotTeam"] = RobotTeam

        self.playera = RPSRobot(self, robots[0], RobotTeam.FIRST)
        self.playerb = RPSRobot(self, robots[1], RobotTeam.SECOND)

        self.playera.init_code()
        self.playerb.init_code()

        self.actions = []
        self.score = {RobotTeam.FIRST: 0, RobotTeam.SECOND: 0}

    def run(self, *args, rounds=1000, **kwargs):
        while len(self.actions) < rounds:
            self.playera.run()
            self.playerb.run()

            actiona = self.playera.globals.get("output", "R")
            actionb = self.playerb.globals.get("output", "R")

            self.actions.append({RobotTeam.FIRST: actiona, RobotTeam.SECOND: actionb})

            if actiona == beat[actionb]:  # A won
                self.score[RobotTeam.FIRST] += 1
            if beat[actiona] == actionb:  # B won
                self.score[RobotTeam.SECOND] += 1

        return self.score
