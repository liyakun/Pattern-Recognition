import matplotlib.pyplot as plt


class Plot2dData:

    def __init__(self):
        pass

    def plot_data_2d(self, X, filename=None):
        """Create a 2D plot, with legend
        """
        # create a figure and its axes
        fig = plt.figure()
        axs = fig.add_subplot(111)

        # plot the data
        axs.plot(X[0, :], X[1, :], 'ro', label='data')

        # set x and y limits of the plotting area
        x_min = X[0, :].min()
        x_max = X[0, :].max()
        axs.set_xlim(x_min-10, x_max+10)
        axs.set_ylim(-2, X[1, :].max()+10)

        # set properties of the legend of the plot
        leg = axs.legend(loc='upper left', shadow=True, fancybox=True, numpoints=1)
        leg.get_frame().set_alpha(0.5)

        # either show figure on screen or write it to disk
        if filename is None:
            plt.show()
        else:
            plt.savefig(filename, facecolor='w', edgecolor='w',
                        papertype=None, format='pdf', transparent=False,
                        bbox_inches='tight', pad_inches=0.1)
        plt.close()