import matplotlib.pyplot as plt


class Gradation(object):
    """
    Gradation of soil.
    """

    def __init__(self):
        self._data = list()

    def set(self, min_diameter, max_diameter, weight):
        """
        Set the weight of a soil fraction.
        :param min_diameter: The minimum diameter of the soil fraction.
        :param max_diameter: The maximum diameter of the soil fraction.
        :param weight: The weight of the soil fraction.
        :return:
        """
        assert max_diameter > min_diameter > 0
        self._data.append((min_diameter, max_diameter, weight))

    @property
    def total_weight(self):
        return sum((i for _, _, i in self._data))

    def get(self, diameter):
        """
        Get the percentage of the soil.
        :param diameter: The diameter to get.
        :return: A float from 0 t0 1.
        >>> g = Gradation()
        >>> g.set(0.005, 0.01, 1)
        >>> g.set(0.01, 0.05, 2)
        >>> g.set(0.05, 0.1, 3)
        >>> g.set(0.1, 0.2, 2)
        >>> g.set(0.2, 0.5, 1)
        >>> g.set(0.5, 2, 1)
        >>> g.get(0.5)

        """
        data = sorted(self._data, key=lambda i: i[0])
        print(data)

    def draw(self):
        pass
