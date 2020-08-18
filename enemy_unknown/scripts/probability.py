import numpy as np


def at_least_one_hit(to_hit, max_shots):
    """
    Returns the chance to get at least one hit if the turns is spent shooting.
    """
    accuracy = to_hit
    if accuracy > 1:
        accuracy = 1
    chance = 1 - (1 - accuracy) ** max_shots
    return float(np.complex128(chance))
