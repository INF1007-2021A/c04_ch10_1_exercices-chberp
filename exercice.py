#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import math

import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:

    return np.linspace(start=-1.3, stop=2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    rayon = (cartesian_coordinates[0] ** 2 + cartesian_coordinates[1] ** 2) ** 1/2
    angle = math.atan(cartesian_coordinates[1]/cartesian_coordinates[0])

    return np.array(rayon, angle)


def find_closest_index(values: np.ndarray, number: float) -> int:

    return (np.abs(values - number)).argmin()


def sine_graphic():
    

    return None


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
