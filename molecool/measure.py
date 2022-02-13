"""
This module is for functions that calculate messurements

"""

import numpy as np

def calculate_distance(rA, rB):
    """
    Function calculates the distance between 2 points.

    Parameters
    ----------
    rA,rB : np.array
        The coordinate of each point

    Returns
    -------
    dist : float
        The distance between the 2 points.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([0,1,0])
    >>> calculate_distance(r1,r2)
    1.0
    """
    # This function calculates the distance between two points given as numpy arrays.
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta