import numpy as np
from lib import Plot2dData
from math import log,exp
from scipy import linalg


class Task13:
    """Implement the task 1.3
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
        x_raw = [i+1 for i in range(len(raw))]

        #hist->independent observations
        x  = [k for el in xrange(1,len(raw)+1) for k in [el]*el]
        hs = [raw[i-1] for i in x]

        N = len(x)
        epochs = range(10)
        arr = np.mat([1,1]).T
        for e in epochs:
            k = arr[0,0]
            a = arr[1,0]
            sdatok = sum([pow(d/a,k) for d in hs])
            sldatok = sum([pow(d/a,k)*log(d/a) for d in hs])
            dldk = N/k - N*log(a) + sum([log(d) for d in hs]) - sldatok
            dlda = (k/a)*(sdatok-N)
            d2ldk2 = -N/(k*k) - sum([pow(d/a,k)*pow(log(d/a),2) for d in hs])
            d2lda2 = (k/(a*a))*(N-(k+1)*sdatok)
            d2ldkda = -N*a+(1/a)*sdatok + (k/a)*sldatok
            hessian = np.mat([[d2ldk2,d2ldkda],[d2ldkda,d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + linalg.inv(hessian)*gr


        distribution = [k/a * pow(el/a, k-1) * (exp(-pow(el/a, k))) for el in x_raw]
        # plot and write to disk
        x_matrix = np.vstack((x_raw, distribution))
        Plot2dData().plot_data_2d(x_matrix, '../results/task13/plotQueries.pdf')



