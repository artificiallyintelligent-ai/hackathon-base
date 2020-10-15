# Usage:
# python -m hackathon
#                       game
#                       bots...
#                       [- [game args...]]
#                       [[--game key] [game values...]...]

if __name__ == "__main__":
    import argparse
    import importlib
    import hackathon

    parser = argparse.ArgumentParser()
    parser.add_argument("game", help="Game to play")
    parser.add_argument("bots", nargs="+", help="Bots playing")

    args, other_args = parser.parse_known_args()

    module = importlib.import_module(args.game)

    games = [game for game in vars(module).values() if type(game) is type if hackathon.Game in game.mro()]

    bots = []
    game_args = []
    argument = False
    for botname in args.bots:
        if botname == "-":
            argument = True
        elif argument:
            try:
                botname = int(botname)
            except ValueError:
                try:
                    botname = float(botname)
                except ValueError:
                    if botname.lower() in ["yes", "true",]:
                        botname = True
                    elif botname.lower() in ["no", "false",]:
                        botname = False
            game_args.append(botname)
        else:
            with open(botname) as f:
                bots.append(f.read())

    game_kwargs = {}
    keyword = False
    for arg in other_args:
        if arg.startswith("-"):
            keyword = arg.lstrip("-")
            game_kwargs[keyword] = []
        else:
            game_kwargs[keyword].append(arg)

    for key, value in game_kwargs.items():
        if len(value) == 0:
            game_kwargs[key] = True
        else:
            values2 = []
            for v in value:
                try:
                    v2 = int(v)
                except ValueError:
                    try:
                        v2 = float(v)
                    except ValueError:
                        if v.lower() in ["yes", "true",]:
                            v2 = True
                        elif v.lower() in ["no", "false",]:
                            v2 = False
                        else:
                            v2 = v
                values2.append(v2)
            game_kwargs[key] = values2

        if len(value) == 1:
            game_kwargs[key] = game_kwargs[key][0]

    game = games[0](bots, *game_args, **game_kwargs)
    print(game.run(*game_args, **game_kwargs))
