"""
We need the p norm, basic idea:
    1. draw all the possible point with x = 1, ||1|| with p = 1/2
    2. when p = 0.5, the Minkoski violates the triangle
"""
from lib import PlotCircle

class Task14:

    def __init__(self):
        pass

    def plot_circle(self, p_value):
        PlotCircle().plot_circle('../results/task14/circle.pdf', p_value)
