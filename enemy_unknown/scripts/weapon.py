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
