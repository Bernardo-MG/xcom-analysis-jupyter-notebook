import numpy as np


def at_least_one_hit(group):
    """
    Returns the chance to get at least one hit if the turns is spent shooting.
    """
    accuracy = group["final_accuracy"]
    if accuracy > 1:
        accuracy = 1
    chance = 1 - (1 - accuracy) ** group["turn_max_shots"]
    return float(np.complex128(chance))
