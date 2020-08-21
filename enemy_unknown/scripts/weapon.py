import math
from decimal import Decimal
from .probability import roll_chance


def max_shots(group):
    """
    Returns the max number of shots a weapon can achieve in a turn.

    Takes into consideration that the weapon may have to reload.
    """
    fire_actions = int(100 / group["time_units"])
    shots = fire_actions * group["burst"]

    if shots > group["capacity"]:
        # Shoots above capacity. Has to reload

        # We have 100 TU. This is used to calculate the max number of shots
        reload_shots = int(100 / group["time_units"])
        if reload_shots > 1:
            # Adds cost to reload between shots
            reload_cost = (reload_shots - 1) * 15
            # The cost will be averaged to each shot
            reload_cost = reload_cost / reload_shots
        else:
            # A single shot. No reload needed
            reload_cost = 0
        cost = group["time_units"] + reload_cost
        fire_actions = int(100 / cost)
        shots = fire_actions * group["burst"]

    return shots


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
    min_prop = 0
    max_prop = 2

    min_damage = min_prop * damage
    max_damage = max_prop * damage

    return roll_chance(Decimal(min_damage), Decimal(max_damage), Decimal(armor))


def penetrating_damage(base_damage, armor):
    """
    Returns the damage after applying armor.
    """
    min_prop = 0
    max_prop = 2

    min_damage = min_prop * base_damage
    max_damage = max_prop * base_damage

    if armor >= max_damage:
        damage = 0
    elif armor < min_damage:
        damage = base_damage
    else:
        # To ease handling the minimal damage we will normalize values
        max_damage_norm = max_damage - min_damage
        armor_norm = armor - min_damage

        # The damage required to actually damage the target with 1 point
        lowest_valid_damage = armor_norm + 1
        # The number of damage values which can damage the target
        damage_range = max_damage_norm - lowest_valid_damage
        # Proportion of the full damage spectrum which can actually damage the target
        to_damage = damage_range / max_damage_norm
        #
        damage = damage_range * to_damage / 2

    return damage


def hits_to_kill(damage, health):
    """
    Returns the number of hits it takes to kill the target.
    """
    if damage > 0:
        hits = health / damage
    else:
        hits = 1000

    if hits < 1:
        hits = 1
    else:
        hits = math.ceil(hits)

    return hits
