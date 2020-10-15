import enum


def get_side():
    pass


def get_turn():
    pass


def get_action(turn: int, side: "RobotTeam"):
    pass


class RobotTeam(enum.Enum):
    FIRST = enum.auto()
    SECOND = enum.auto()
