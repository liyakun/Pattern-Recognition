import matplotlib.pyplot as plt
from numpy import linspace, vstack, zeros, hstack
from scipy.stats import norm
import matplotlib.lines as mlines


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

    def plot_data_density(self, X, filename=None):

        # fit a normal distribution to the data
        mean, std = norm.fit(X)

        # create a figure with fixed size, and its axes
        fig1 = plt.figure(1, figsize=(14, 14))
        axs = fig1.add_subplot(111)

        # plot the pdf
        x = linspace(140, 210, 100)
        p = norm.pdf(x, mean, std)
        axs.plot(x, p, 'k', linewidth=2, color='y')
        title = "Fit Results: mean = %.2f,  std = %.2f" % (mean, std)
        plt.title(title)

        # plot the actual data, set y=0 for all points
        X = vstack((X, zeros(len(X))))
        axs.plot(X[0, :], X[1, :], 'ro', label='data', color='blue')

        # add legend
        plt.plot([], label="normal", color="yellow")
        f2 = axs.legend(loc=1, shadow=True, fancybox=True, numpoints=1)
        f2.get_frame().set_alpha(0.5)

        # either show figure on screen or write it to disk
        if filename is None:
            fig1.show()
        else:
            fig1.savefig(filename, facecolor='w', edgecolor='w',
                        papertype=None, format='pdf', transparent=False,
                        bbox_inches='tight', pad_inches=0.1)

        plt.close()