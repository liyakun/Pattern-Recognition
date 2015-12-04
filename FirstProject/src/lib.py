import matplotlib.pyplot as plt
from numpy import linspace, vstack, zeros, arange, power, abs
from scipy.stats import norm
import bonus


class Plot2dData:

    def __init__(self):
        pass

    def plot_data_2d(self, X, task, distribution, filename=None):
        """Create a 2D plot, with legend
        """

        # create a figure and its axes
        fig = plt.figure()
        axs = fig.add_subplot(111)

        if task == str(3):
            axs.plot(X[0, :], X[1, :], 'k-', label='data')
            axs.plot(distribution, color='red')
        elif task == str(1):
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


class PlotCircle:

    def __init__(self):
        pass

    def plot_circle(self, filename, p_value):
        """Plot circle by solving the circle function:
            |x|^p + |y|^p = 1
            |y|^p = 1 - |x|^p
        """
        x = arange(-1.0, 1.0, 0.0000001)
        y_1 = power((1 - power(abs(x), p_value)), 1/float(p_value))
        y_2 = -power((1 - power(abs(x), p_value)), 1/float(p_value))

        fig = plt.gcf()
        title = "p value is: %.2f" % p_value
        plt.title(title)

        plt.plot(x, y_1, color='blue')
        plt.plot(x, y_2, color='blue')
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        fig.savefig(filename)


    def plot_circle_ai(self, filename, p_value):
        """
        """

        STEP = 0.01
        x = y = arange(STEP, 1.0, STEP)
        points = [(a, b, 1 - a - b) for a in x for b in y if (a+b) < 1]
        p = [el for el in points if abs(bonus.Bonus().cal_distance(el, (1/3, 1/3, 1/3))) - 1 < 0.001]


        fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        ax = fig.add_subplot(111)

        for x, y, z in points:
            # ax.scatter(x, y, z)
            ax.scatter(x, y)

        for x, y, z in p:
            ax.scatter(x, y, color='red')
            # ax.scatter(x, y, z, color='red')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # ax.set_zlabel('Z Label')
        fig.savefig(filename)