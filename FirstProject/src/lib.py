import matplotlib.pyplot as plt
from numpy import linspace, vstack, zeros, arange, power, abs
from mpl_toolkits.mplot3d import axes3d
from scipy.stats import norm
import bonus
import random


class Plot2dData:
    """
    Plot 2d data points
    """
    def __init__(self):
        pass

    def plot_data_2d(self, X, task, distribution, filename=None):
        """
        :param X: the data matrix we want to plot
        :param task: task 1 or task 3
        :param distribution: for task 3's Weibull distribution
        :param filename: file name for the plot
        :return:
        """
        # create a figure and its axes
        fig = plt.figure()
        axs = fig.add_subplot(111)
        if task == str(3):  # task 3
            axs.plot(X[0, :], X[1, :], 'k-', label='data')
            axs.plot(distribution, color='red')
        elif task == str(1):    # task 1
            axs.plot(X[0, :], X[1, :], 'ro', label='data')
        else:
            raise ValueError('The value of "task" should be 1 or 3.')
        # set x and y limits of the plotting area
        x_min = X[0, :].min()
        x_max = X[0, :].max()
        axs.set_xlim(x_min-10, x_max+10)
        axs.set_ylim(-2, X[1, :].max()+10)
        # set properties of the legend of the plot
        leg = axs.legend(loc='upper left', shadow=True, fancybox=True, numpoints=1)
        # set the alpha value of the legend: it will be translucent
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
    """
    Fit and plot the normal distribution to 1D data
    """
    def __init__(self):
        pass

    def plot_data_density(self, X, filename=None):
        """
        :param X: data used for fit
        :param filename: file name to write to disk
        :return:
        """
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
        # plot the data
        axs.plot(X[0, :], X[1, :], 'ro', label='data', color='blue')
        # plot label of legend for the distribution
        plt.plot([], label="normal", color="yellow")
        # set the legend to location upper right
        f2 = axs.legend(loc=1, shadow=True, fancybox=True, numpoints=1)
        # set the alpha value of the legend: it will be translucent
        f2.get_frame().set_alpha(0.5)
        # either show figure on screen or write it to disk
        if filename is None:
            fig1.show()
        else:
            fig1.savefig(filename, facecolor='w', edgecolor='w',
                        papertype=None, format='pdf', transparent=False,
                        bbox_inches='tight', pad_inches=0.1)

        plt.close()


class PlotCircle:
    """
    This class implement the circle plot fot task 1.4 and bonus task
    """
    def __init__(self):
        pass

    def plot_circle(self, filename, p_value):
        """
        :param filename: file name of the plot write to disk
        :param p_value: p value
        :return:
        """
        # set the range of x axis
        x = arange(-1.0, 1.0, 0.00001)
        #  plot circle by solving the circle function: |x|^p + |y|^p = 1, |y|^p = 1 - |x|^p
        y_1 = power((1 - power(abs(x), p_value)), 1/float(p_value))
        # get the lower part of the circle
        y_2 = -y_1

        fig = plt.gcf()
        title = "p value is: %.2f" % p_value
        plt.title(title)

        plt.plot(x, y_1, color='blue')
        plt.plot(x, y_2, color='blue')
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        fig.savefig(filename)

    def plot_circle_ai(self, filename, p_value):
        """plot the circle in Aitchison geometry
        :param filename: file name for the plot
        :param p_value: p value
        :return:
        """
        # set the range of x, y ,z axis
        x = y = z = arange(0.0, 1.0, 0.01)
        # get the points of the S^3 vector space
        points = [(a, b, c) for a in x for b in y for c in z if (a + b + c == 1) and a > 0 and b > 0 and c > 0]
        # get the circle centered at (a, b, c) position with radius r by approximation
        circle_points = [el for el in points if abs(bonus.Bonus().cal_distance(el, (0.4, 0.2, 0.4)) - 0.5) <
                         0.025]
        fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')    # plot 3d object
        ax = fig.add_subplot(111)                       # plot 2d
        points = random.sample(points, 500)             # reduce the number of points to be plotted to make plot faster

        for x, y, z in points:  # points in the space
            # ax.scatter(x, y, z)
            ax.scatter(x, y)    # project to 2d

        for x, y, z in circle_points:   # points in the circle
            # ax.scatter(x, y, z, color='red')
            ax.scatter(x, y, color='red')   # project to 2d

        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        # ax.set_zlim([0, 1])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # ax.set_zlabel('Z Label')
        fig.savefig(filename)
