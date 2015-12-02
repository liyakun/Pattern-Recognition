from lib import PlotCircle
import numpy as np

class Bonus:

    def __int__(self):
        pass

    def cal_closure(self, v_x):
        return v_x / sum(v_x)

    # circle mutiply
    def cal_powering(self, v_x,a):
        return self.cal_closure([np.power(x, a) for x in v_x])

    # circle plus
    def cal_perturbation(self, v_x, v_y):
        return self.cal_closure([x * y for x in v_x for y in v_y])

    def cal_inner_product(self, v_x, v_y):
        return (1.0) / 2 * len(v_x) * sum([np.log(v_x[i]) * np.log(v_y[j]) for i in len(v_y) for j in len(v_y)])

    def cal_norm(self, v_x):
        return np.sqrt(self.cal_inner_product(v_x, v_x))

    def circle_minus(self, v_x, v_y):
        return self.cal_perturbation(v_x, self.cal_powering(-1, v_y))

    def cal_distance(self, v_x, v_y):
        return self.cal_norm(self.circle_minus(v_x, v_y))


    def bonus(self):
        PlotCircle().plot_circle_ai('../results/bonus/circle.pdf', 2)