import lib
import numpy as np


class Bonus:
    """
    implement the bonus task
    """

    def __int__(self):
        pass

    def cal_closure(self, v_x):
        return [i / sum(v_x) for i in v_x]

    # circle plus
    def cal_perturbation(self, v_x, v_y):
        return self.cal_closure([x * y for x, y in zip(v_x, v_y)])

    def cal_inner_product(self, v_x, v_y):
        length = len(v_x)
        return 1.0 / (2.0 * length) * sum([np.log(v_x[i]/v_x[j]) * np.log(v_y[i]/v_y[j]) for i in range(length) for j in
                                           range(length)])

    def cal_norm(self, v_x):
        return np.sqrt(self.cal_inner_product(v_x, v_x))

    # circle mutiply
    def cal_powering(self, v_x, a):
        return self.cal_closure([np.power(x, a) for x in v_x])

    def cal_minus(self, v_x, v_y):
        return self.cal_perturbation(v_x, self.cal_powering(v_y, -1))

    def cal_distance(self, v_x, v_y):
        return self.cal_norm(self.cal_minus(v_x, v_y))

    def bonus(self):
        lib.PlotCircle().plot_circle_ai('../results/bonus/circle.pdf', 2)
