import numpy as np
from lib import Plot2dData


class Task11:
    """Implement the task 1.1
    """

    def __init__(self):
        pass

    def read_and_plot(self):
        """
        read weight, height and gender information from file, and plot weight against height
        """
        dt = np.dtype([('w', np.float), ('h', np.float), ('g', np.str_, 1)])
        data = np.loadtxt('../resources/whData.dat', dtype=dt, comments='#', delimiter=None)

        # read weight, height, and gender information into 1D arrays
        ws = np.array([d[0] for d in data])
        hs = np.array([d[1] for d in data])

        # remove data with negative value
        hs = np.delete(hs, np.where(ws < 0), None)
        ws = np.delete(ws, np.where(ws < 0), None)

        x_matrix = np.vstack((ws, hs))
        print x_matrix
        Plot2dData().plot_data_2d(x_matrix, '../results/task11/plotWH.pdf')

        x_matrix = x_matrix.transpose()
        # exchange first and second columns
        x_matrix[:, [0, 1]] = x_matrix[:, [1, 0]]
        Plot2dData().plot_data_2d(x_matrix.transpose(), '../results/task11/plotHW.pdf')
