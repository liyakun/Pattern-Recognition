import numpy as np
from lib import Plot2dData
from math import log, exp
from scipy import linalg


class Task13:
    """Implement the task 1.3
    """

    def __init__(self):
        pass

    def read_and_plot_opt(self):
        """
        read weight, height and gender information from file, and plot weight against height
        """
        dt = np.dtype([('date', np.str_, 24), ('queries', np.int)])
        data = np.loadtxt('../resources/myspace.csv', dtype=dt, comments='#', delimiter=',')

        # read queries information into 1D array
        raw = [d[1] for d in data if d[1] != 0]
        x_raw = [i+1 for i in range(len(raw))]

        N = sum(raw)

        epochs = range(20)
        arr = np.mat([1.0, 1.0]).T
        for e in epochs:
            k = arr[0, 0]
            a = arr[1, 0]

            sldatok = sum([h * np.power((x / a), k) * log(x / a) for h, x in zip(raw, x_raw)])
            sdatok = sum([h * np.power((x / a), k) for h, x in zip(raw, x_raw)])
            sd2ldk2 = sum([h * np.power((x / a), k) * pow(log(x / a), 2) for h, x in zip(raw, x_raw)])
            slogd = sum([h * log(x) for h, x in zip(raw, x_raw)])

            dldk = N/k - N*log(a) + slogd - sldatok
            dlda = (k/a)*(sdatok-N)
            d2ldk2 = -N/(k*k) - sd2ldk2
            d2lda2 = (k/(a*a))*(N-(k+1)*sdatok)
            d2ldkda = (1/a)*sdatok + (k/a)*sldatok - N/a

            hessian = np.mat([[d2ldk2, d2ldkda], [d2ldkda, d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + np.dot(linalg.inv(hessian), gr)

        #distribution scaled by N
        distribution = [(N*(k/a * pow(el/a, k-1) * (exp(-pow(el/a, k))))) for el in x_raw]

        # plot and write to disk
        x_matrix = np.vstack((x_raw, raw))
        Plot2dData().plot_data_2d(x_matrix, '3', distribution, '../results/task13/plotQueries.pdf')



    def read_and_plot(self):
        """
        read weight, height and gender information from file, and plot weight against height
        """
        dt = np.dtype([('date', np.str_, 24), ('queries', np.int)])
        data = np.loadtxt('../resources/myspace.csv', dtype=dt, comments='#', delimiter=',')

        # read queries information into 1D array
        raw = [d[1] for d in data if d[1] != 0]
        x_raw = [i+1 for i in range(len(raw))]

        # hist->independent observations
        hs = [i for idx, value in enumerate(raw) for i in ([x_raw[idx]] * value)]

        N = len(hs)
        epochs = range(20)
        arr = np.mat([1.0, 1.0]).T
        for e in epochs:
            k = arr[0, 0]
            a = arr[1, 0]

            sdatok = sum([pow(d/a, k) for d in hs])
            sldatok = sum([pow(d/a, k)*log(d/a) for d in hs])

            dldk = N/k - N*log(a) + sum([log(d) for d in hs]) - sldatok
            dlda = (k/a)*(sdatok-N)

            d2ldk2 = -N/(k*k) - sum([pow(d/a, k)*pow(log(d/a), 2) for d in hs])
            d2lda2 = (k/(a*a))*(N-(k+1)*sdatok)

            d2ldkda = (1/a)*sdatok + (k/a)*sldatok - N/a

            hessian = np.mat([[d2ldk2, d2ldkda], [d2ldkda, d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + np.dot(linalg.inv(hessian), gr)

        #distribution scaled by N
        distribution = [(N*(k/a * pow(el/a, k-1) * (exp(-pow(el/a, k))))) for el in x_raw]

        # plot and write to disk
        x_matrix = np.vstack((x_raw, raw))
        Plot2dData().plot_data_2d(x_matrix, '3', distribution, '../results/task13/plotQueries.pdf')
