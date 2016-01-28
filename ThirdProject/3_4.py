import numpy as np
import numpy.linalg as la
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt


dt = np.dtype([('w', np.float), ('h', np.float), ('g', 'S1')])
data = np.loadtxt('resources/whData.dat', dtype=dt, comments='#', delimiter=None)

hgt = data['w']
wgt = data['h']

xmin = hgt.min()-15
xmax = hgt.max()+15
ymin = wgt.min()-15
ymax = wgt.max()+15

fig = plt.figure()
axs1 = fig.add_subplot(141)
axs2 = fig.add_subplot(142)
axs3 = fig.add_subplot(143)
axs4 = fig.add_subplot(144)



def trsf(x):
	return x / 100.

n = 10
x = np.linspace(xmin, xmax, 100)

# method 1:
# regression using ployfit
c = poly.polyfit(hgt, wgt, n)
y = poly.polyval(x, c)

axs1.set_title("ployfit")
axs1.plot(hgt, wgt, 'ko', x, y, 'r-')
axs1.set_xlim(xmin,xmax)
axs1.set_ylim(ymin,ymax)


# method 2:
# regression using the Vandermonde matrix and pinv
X = poly.polyvander(hgt, n)
c = np.dot(la.pinv(X), wgt)
y = np.dot(poly.polyvander(x,n), c)

axs2.set_title("Vandermonde and pinv")
axs2.plot(hgt, wgt, 'ko', x, y, 'r-')
axs2.set_xlim(xmin,xmax)
axs2.set_ylim(ymin,ymax)

# method 3:
# regression using the Vandermonde matrix and lstsq

X = poly.polyvander(hgt, n)
c = la.lstsq(X, wgt)[0]
y = np.dot(poly.polyvander(x,n), c)

axs3.set_title("Vandermonde and lstsq")
axs3.plot(hgt, wgt, 'ko', x, y, 'r-')
axs3.set_xlim(xmin,xmax)
axs3.set_ylim(ymin,ymax)

# method 4:
# regression on transformed data using the Vandermonde
# matrix and either pinv or lstsq
X = poly.polyvander(trsf(hgt), n)
c = np.dot(la.pinv(X), wgt)
y = np.dot(poly.polyvander(trsf(x),n), c)

axs4.set_title("transformed data using Vandermonde")
axs4.plot(hgt, wgt, 'ko', x, y, 'r-')
axs4.set_xlim(xmin,xmax)
axs4.set_ylim(ymin,ymax)

plt.show()