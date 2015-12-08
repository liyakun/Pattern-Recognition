import numpy as np
from lib import Plot2dData
from math import log, exp
from scipy import linalg


class Task13:
    """Implement the task 1.3, with optimized solution and basic solution by creating long list of d_i
    """

    def __init__(self):
        pass

    def read_and_plot_opt(self):
        """read the data from mysapce.csv, and calculate the math formula base on histogram and X, without creating long
        list of d_i
        """
        dt = np.dtype([('date', np.str_, 24), ('queries', np.int)])
        data = np.loadtxt('../resources/myspace.csv', dtype=dt, comments='#', delimiter=',')
        raw = [d[1] for d in data if d[1] != 0]  # read queries information into 1D array
        x_raw = [i+1 for i in range(len(raw))]  # create a list of sequential numbers
        N = sum(raw)    # get the sum of all the values in second column

        epochs = range(20)  # set the number of iterations
        arr = np.mat([1.0, 1.0]).T  # set the initial value of k and alpha
        for e in epochs:
            k = arr[0, 0]
            a = arr[1, 0]

            # get the common parts of the derivative functions
            sldatok = sum([h * np.power((x / a), k) * log(x / a) for h, x in zip(raw, x_raw)])
            sdatok = sum([h * np.power((x / a), k) for h, x in zip(raw, x_raw)])
            sd2ldk2 = sum([h * np.power((x / a), k) * pow(log(x / a), 2) for h, x in zip(raw, x_raw)])
            slogd = sum([h * log(x) for h, x in zip(raw, x_raw)])

            # compute each part base on the math formula of the project document
            dldk = N/k - N*log(a) + slogd - sldatok
            dlda = (k/a)*(sdatok-N)
            d2ldk2 = -N/(k*k) - sd2ldk2
            d2lda2 = (k/(a*a))*(N-(k+1)*sdatok)
            d2ldkda = (1/a)*sdatok + (k/a)*sldatok - N/a
            hessian = np.mat([[d2ldk2, d2ldkda], [d2ldkda, d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + np.dot(linalg.inv(hessian), gr)

        # distribution scaled by N, as "N * probability = frequency"
        distribution = [(N*(k/a * pow(el/a, k-1) * (exp(-pow(el/a, k))))) for el in x_raw]
        # plot and write to disk
        x_matrix = np.vstack((x_raw, raw))
        Plot2dData().plot_data_2d(x_matrix, '3', distribution, '../results/task13/plotQueries.pdf')

    def read_and_plot(self):
        """get data from myspace.csv and drawing Weibull distribution by creating a long list of d_i
        """
        dt = np.dtype([('date', np.str_, 24), ('queries', np.int)])
        data = np.loadtxt('../resources/myspace.csv', dtype=dt, comments='#', delimiter=',')
        # read queries information into 1D array
        raw = [d[1] for d in data if d[1] != 0]
        x_raw = [i+1 for i in range(len(raw))]
        # hist->independent observations
        hs = [i for idx, value in enumerate(raw) for i in ([x_raw[idx]] * value)]
        N = len(hs) # number of observations
        epochs = range(20)  # number of iterations to get k and alpha
        arr = np.mat([1.0, 1.0]).T  # set initial value of k and a
        for e in epochs:
            k = arr[0, 0]
            a = arr[1, 0]
            # get the common parts of the formula to calculate
            sdatok = sum([pow(d/a, k) for d in hs])
            sldatok = sum([pow(d/a, k)*log(d/a) for d in hs])

            # derive the formula based on the project document
            dldk = N/k - N*log(a) + sum([log(d) for d in hs]) - sldatok
            dlda = (k/a)*(sdatok-N)
            d2ldk2 = -N/(k*k) - sum([pow(d/a, k)*pow(log(d/a), 2) for d in hs])
            d2lda2 = (k/(a*a))*(N-(k+1)*sdatok)
            d2ldkda = (1/a)*sdatok + (k/a)*sldatok - N/a
            hessian = np.mat([[d2ldk2, d2ldkda], [d2ldkda, d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + np.dot(linalg.inv(hessian), gr)
        # distribution scaled by N, as "N * probability = frequency"
        distribution = [(N*(k/a * pow(el/a, k-1) * (exp(-pow(el/a, k))))) for el in x_raw]
        # plot and write to disk
        x_matrix = np.vstack((x_raw, raw))
        Plot2dData().plot_data_2d(x_matrix, '3', distribution, '../results/task13/plotQueries.pdf')
