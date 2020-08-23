import math


def max_actions(points, action_cost, recover_cost, limit):
    """
    Returns the max number of actions. It will weight the action cost against the available points, adding the
    recovery cost each time it runs out of points.
    """
    if limit <= 0:
        actions = 0
    elif action_cost <= 0:
        actions = 0
    else:
        fire_actions = int(points / action_cost)
        actions = fire_actions

        if actions > limit:
            # Shoots above capacity. Has to reload

            # We need to check the number of times the weapon has to reload
            reload_shots = fire_actions
            if reload_shots > 1:
                # Adds cost to reload between shots
                reload_cost = (reload_shots - 1) * recover_cost
                # The cost will be averaged to each shot
                reload_cost = reload_cost / reload_shots
            else:
                # A single shot. No reload needed
                reload_cost = 0
            cost = action_cost + reload_cost
            fire_actions = int(points / cost)
            actions = fire_actions

    return actions
