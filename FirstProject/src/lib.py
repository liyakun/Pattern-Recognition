import matplotlib.pyplot as plt
from numpy import linspace, zeros_like, sqrt, pi, exp
from scipy.stats import norm


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


class PlotDataDensity:

    def __init__(self):
        pass

    def plot_data_density(self, X, mu, sigma, filename=None):
        # val = 0
        # plt.plot(X, zeros_like(X) + val, 'x')

        # p = norm.pdf(mu, std)
        # plt.plot(p, 'k', linewidth=2)
        counts, bins, ignored = plt.hist(X)
        plt.plot(bins, 1/(sigma * sqrt(2 * pi)) * exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
        title = "Fit Results: mu = %.2f,  std = %.2f" % (mu, sigma)
        plt.title(title)

        # either show figure on screen or write it to disk
        if filename is None:
            plt.show()
        else:
            plt.savefig(filename, facecolor='w', edgecolor='w',
                        papertype=None, format='pdf', transparent=False,
                        bbox_inches='tight', pad_inches=0.1)