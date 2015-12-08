import numpy as np
from lib import PlotDataDensity


class Task12:
    """Implement the task 1.2
    """

    def __init__(self):
        pass

    def read_and_plot(self):
        """
        read weight, height and gender information from file, and fitting a Normal distribution to body size
        """
        dt = np.dtype([('w', np.float), ('h', np.float), ('g', np.str_, 1)])
        data = np.loadtxt('../resources/whData.dat', dtype=dt, comments='#', delimiter=None)
        # read height size information into 1D arrays
        hs = np.array([d[1] for d in data])
        # plot and write to disk
        PlotDataDensity().plot_data_density(hs, '../results/task12/density.pdf')