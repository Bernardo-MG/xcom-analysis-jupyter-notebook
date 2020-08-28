import math
from scipy.stats import randint
from .probability import roll_chance, roll_success_range
from .action import max_actions


def max_shots(group):
    """
    Returns the max number of shots a weapon can achieve in a turn.

    Takes into consideration that the weapon may have to reload.
    """

    return max_actions(100, group["time_units"], 15, group["burst"])


def burst(group):
    """
    Returns the number of shots the fire mode will make.
    """

    if group["fire_mode"] == "auto":
        shots = 3
    else:
        shots = 1

    return shots


def chance_to_damage(damage, armor):
    """
    Returns the chance to damage against the received armor.
    """
    min_prop = 0.5
    max_prop = 1.5

    min_damage = min_prop * damage
    max_damage = max_prop * damage

    damage_range = randint(min_damage, max_damage + 1)
    return damage_range.sf(armor)


def penetrating_damage(base_damage, armor):
    """
    Returns the damage after applying armor.
    """
    min_prop = 0.5
    max_prop = 1.5

    min_damage = min_prop * base_damage
    max_damage = max_prop * base_damage

    values = roll_success_range(min_damage, max_damage, armor, normalize=True)

    if values:
        damage = (values["min"] + values["max"]) / 2
    else:
        damage = 0

    return damage


def hits_to_kill(damage, health):
    """
    Returns the number of hits it takes to kill the target.
    """
    if damage > 0:
        hits = health / damage
    else:
        hits = math.inf

    if hits < 1:
        hits = 1
    elif hits < math.inf:
        hits = math.ceil(hits)

    return hits
