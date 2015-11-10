import numpy as np
from lib import Plot2dData
from itertools import chain


class Task13:
    """Implement the task 1.2
    """

    def __init__(self):
        pass

    def read_and_plot(self):
        """
        read weight, height and gender information from file, and plot weight against height
        """
        dt = np.dtype([('date', np.str_, 24), ('queries', np.int)])
        data = np.loadtxt('../resources/myspace.csv', dtype=dt, comments='#', delimiter=',')

        # read queries information into 1D array
        raw = [d[1] for d in data if d[1] != 0]

        #hist->independent observations
        x  = [k for el in xrange(1,len(raw)+1) for k in [el]*el]
        hs = [raw[i-1] for i in x]


        # plot and write to disk
        x_matrix = np.vstack((x, hs))
        Plot2dData().plot_data_2d(x_matrix, '../results/task13/plotQueries.pdf')


