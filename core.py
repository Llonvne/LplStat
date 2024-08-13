import data
import copy


def resolve_team(team, registry):
    if isinstance(team, int):
        for t in data.status:
            if t['summerRank'] == team:
                return t
        raise KeyError(team, "not found")
    else:
        return registry[team]


def next_game(game):
    num = int(game[1:])
    if num != 12:
        return "G" + str(num + 1)
    else:
        return None


def rank(e):
    return {1: e["G12W"],
            2: e["G12L"],
            3: e["G11L"],
            4: e["G10L"],
            5: e["G5L"],
            6: e["G6L"],
            7: e["G3L"],
            8: e["G4L"],
            9: e["G1L"],
            10: e["G2L"]}


def get_rank_int_by_team(team, rank: dict):
    for index, t in rank.items():
        if t['name'] == team['name']:
            return index
    raise KeyError(team['name'])


__result = []


def __calc(game_name, registry):
    if game_name is None:
        __result.append(registry)
        return
    blue, red = map(
        lambda t: resolve_team(t, registry), data.playoffs[game_name]
    )

    # blue > red

    case1 = copy.deepcopy(registry)

    case1[game_name + "W"] = blue
    case1[game_name + "L"] = red

    __calc(next_game(game_name), case1)

    # red > blue

    case2 = copy.deepcopy(registry)

    case2[game_name + "W"] = red
    case2[game_name + "L"] = blue

    __calc(next_game(game_name), case2)


def calc_all():
    __calc("G1", {})
    global __result
    result = __result
    __result = []
    return result
