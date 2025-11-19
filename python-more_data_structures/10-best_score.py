def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary: A dictionary with string keys and integer values

    Returns:
        The key with the highest value, or None if dictionary is empty or None
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key

    return best_key
