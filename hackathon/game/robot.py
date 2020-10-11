import copy

from hackathon import CodeRunner


def partial(func, instance):
    def inner(*args):
        func(instance, *args)

    return inner


def extract_useful(instance):
    clazz = type(instance)
    funcs = {k: partial(v, instance)
             for k, v in clazz.__dict__.items() if callable(v) if not k.startswith('_')}

    everything_else = {k: instance
                       for k, v in clazz.__dict__.items() if not callable(v) if not k.startswith('_') if
                       k != 'globalcount'}

    funcs.update(everything_else)

    return funcs


class Robot(CodeRunner):
    globalcount = 0

    def __init__(self, game, code: str):
        env = copy.copy(game.env)
        env.globals.update(extract_useful(self))
        print(env.globals)
        super().__init__(env, code)
        self.game = game
        self.id = Robot.globalcount
        Robot.globalcount += 1

    def __hash__(self):
        return self.id
