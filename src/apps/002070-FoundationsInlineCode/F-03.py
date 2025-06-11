def calculate_difference_between_two_dates(date1, date2, difference_type='days'):
    """
    Calculate the difference between two dates in specified units.

    Parameters:
    date1 (datetime): The first date.
    date2 (datetime): The second date.
    difference_type (str): The type of difference to calculate ('days', 'weeks', 'months', 'years', 'hours', 'minutes', 'seconds').

    Returns:
    int: The difference between the two dates in the specified units.
    """

    from datetime import timedelta

    # Calculate the difference in days
    delta = (date2 - date1).days

    if difference_type == 'days':
        return delta
    elif difference_type == 'weeks':
        return delta // 7
    elif difference_type == 'months':
        return (date2.year - date1.year) * 12 + (date2.month - date1.month)
    elif difference_type == 'years':
        return date2.year - date1.year
    elif difference_type == 'hours':
        return delta * 24
    elif difference_type == 'minutes':
        return delta * 24 * 60
    elif difference_type == 'seconds':
        return delta * 24 * 60 * 60
    else:
        raise ValueError("Invalid difference type specified.")

    