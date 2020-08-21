from decimal import Decimal


def at_least_one(chance, attempts):
    """
    Returns the chance to get at least one success on a number of attempts.
    """
    if chance > 1:
        chance = 1

    return Decimal(1 - (1 - chance) ** attempts)


def roll_chance(floor, ceiling, goal, above=True, equal=False):
    """
    Returns the chance to get a value above the goal. This is the same as rolling a dice and trying to get above a
    value.
    """

    # Data will normalized to start at 1
    if floor <= 0:
        diff = 0 - floor + 1
        floor += diff
        ceiling += diff
        goal += diff

    if ceiling == 0:
        chance = 0
    elif goal > ceiling:
        if above:
            chance = 0
        else:
            chance = 1
    elif goal < floor:
        if above:
            chance = 1
        else:
            chance = 0
    else:
        if not above:
            chance = 1 - roll_chance(floor, ceiling, goal, not above, not equal)
        else:
            if equal:
                chance = (goal - 1) / Decimal(ceiling - floor + 1)
            else:
                chance = goal / Decimal(ceiling - floor + 1)

            if chance > 1:
                chance = 1
            elif chance < 0:
                chance = 0

            if above:
                # Success is the inverse of the chance to fail
                chance = 1 - Decimal(chance)
            else:
                chance = Decimal(chance)

    return chance
