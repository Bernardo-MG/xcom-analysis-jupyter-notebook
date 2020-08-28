from scipy.stats import binom


def at_least_one(chance, attempts):
    """
    Returns the chance to get at least one success on a number of attempts.
    """
    if chance > 1:
        chance = 1

    return binom.cdf(attempts, attempts, chance) - binom.cdf(0, attempts, chance)


def roll_success_range(floor, ceiling, goal, above=True, equal=False, normalize=False):
    """
    Returns the range of success on a roll. This means both the interval of valid values and its number.
    """

    valid = True
    if above:
        if equal:
            if goal > ceiling:
                valid = False
            start = goal
        else:
            if goal >= ceiling:
                valid = False
            start = goal + 1

        end = ceiling
    else:
        if equal:
            if goal < floor:
                valid = False
            end = goal
        else:
            if goal <= floor:
                valid = False
            end = goal - 1

        start = floor

    if end > ceiling:
        end = ceiling
    if start < floor:
        start = floor

    if normalize & above:
        distance = (start - floor)
        start -= distance
        end -= distance

    if valid:
        result = {"min": start, "max": end}
    else:
        result = None

    return result
