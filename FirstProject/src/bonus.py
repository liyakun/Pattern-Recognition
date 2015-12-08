import lib
import numpy as np


class Bonus:
    """
    implement the bonus task, common operations in Aitchison geometry here
    """

    def __init__(self):
        pass

    def cal_closure(self, v_x):
        """
        :param v_x: get the closure of v_x
        :return: the value after closure of v_x
        """
        return [i / sum(v_x) for i in v_x]

    def cal_perturbation(self, v_x, v_y):
        """calculate the perturbation of v_x and v_y, and return the calculated value
        """
        return self.cal_closure([x * y for x, y in zip(v_x, v_y)])

    def cal_inner_product(self, v_x, v_y):
        """compute the inner product of v_x and v_y and return it
        """
        length = len(v_x)
        ran = range(length)
        return 1.0 / (2.0 * length) * sum([np.log(v_x[i]/v_x[j]) * np.log(v_y[i]/v_y[j]) for i in ran for j in
                                           ran])

    def cal_norm(self, v_x):
        """compute the norm of v_x and return it
        """
        return np.sqrt(self.cal_inner_product(v_x, v_x))

    def cal_powering(self, v_x, a):
        """compute the powering of v_x to a and return it
        """
        return self.cal_closure([np.power(x, a) for x in v_x])

    def cal_distance(self, v_x, v_y):
        """compute the distance between two vector v_x and v_y
        """
        return self.cal_norm(self.cal_perturbation(v_x, self.cal_powering(v_y, -1)))

    def bonus(self):
        """implement the bonus task
        """
        lib.PlotCircle().plot_circle_ai('../results/bonus/circle.pdf', 2)
