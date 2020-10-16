import copy

import hackathon


def partial(func, instance):
    def inner(*args):
        return func(instance, *args)

    return inner


def extract_useful(instance):
    clazz = type(instance)
    funcs = {k: partial(v, instance)
             for k, v in vars(clazz).items() if callable(v) if not (k.startswith('_') or k.endswith('_'))}
    #                                            function      cannot start or end with '_'

    everything_else = {k: instance
                       for k, v in vars(clazz).items() if not callable(v) if not k.startswith('_') if
                       k != 'globalcount'}

    funcs.update(everything_else)

    return funcs


class Robot(hackathon.CodeRunner):
    globalcount = 0

    def __init__(self, game, code: str):
        env = copy.deepcopy(game.env)
        env.globals.update(extract_useful(self))
        super().__init__(env, code)

        self.game = game  # reference map by self.game.map
        self.id = Robot.globalcount
        Robot.globalcount += 1

    def __hash__(self):
        return self.id
