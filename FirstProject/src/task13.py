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

        #hist->independent observations
        x  = [k for el in xrange(1,len(raw)+1) for k in [el]*el]
        hs = [raw[i-1] for i in x]

        N = len(x)
        epochs = range(10)
        al = pow(np.mean(x),2)/np.var(x);
        la=np.mean(x)/np.var(x)
        arr = np.mat([al,la]).T
        dldk_p = 0
        for e in epochs:
            k = arr[0,0]
            a = arr[1,0]
            dldk = N/k - N*log(a)
            dlda = -N
            d2ldk2 = -N/(k*k)
            d2lda2 = 0
            d2ldkda = -N/a

            for d in hs:
                datok = pow((d/a),k)
                logda = log(d/a)
                dldk += (log(d) - datok*logda)
                dlda   += datok
                d2ldk2 -= datok*logda*logda
                d2lda2 += datok
                d2ldkda = d2ldkda + 1/a * datok + k/a * datok*logda
            dlda*=(k/a)
            d2lda2 = k*(N - (k+1)*d2lda2)/(a*a)
            hessian = np.mat([[d2ldk2,d2ldkda],[d2ldkda,d2lda2]])
            gr = np.mat([-dldk, -dlda]).T
            arr = arr + linalg.inv(hessian)*gr

        distribution = [k/a * pow(el/a,k-1) * (exp(-pow(el/a,k))) for el in hs]
        # plot and write to disk
        x_matrix = np.vstack((x, distribution))
        Plot2dData().plot_data_2d(x_matrix, '../results/task13/plotQueries.pdf')


