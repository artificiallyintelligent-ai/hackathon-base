from .stubs import *

output = ""
history = ""
win = {"R": "P", "P": "S", "S": "R"}

def rchoice(s):
    if not s:
        return "P"
    return s[
        int(get_turn() * 24.542243858834 - 4832.584377 * 7325285848277677.3485 % 3285787478 % (get_turn() + 1))
        % len(s)]


opp_side = {RobotTeam.FIRST: RobotTeam.SECOND, RobotTeam.SECOND: RobotTeam.FIRST}


def turn():
    global history, output
    turn = get_turn()

    if turn == 0:
        output = rchoice("RPS")
        return

    input = get_action(turn - 1, opp_side[get_side()])
    history += input

    output = win[rchoice(history)]
