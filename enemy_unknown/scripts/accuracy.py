def average_to_hit(accuracy):
    """
    Returns the average chance to hit. This will multiply the accuracy by the average soldier accuracy.
    """
    return accuracy / 100 * 0.55
