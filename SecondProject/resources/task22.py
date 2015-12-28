import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

dt = np.dtype([('w', np.float), ('h', np.float), ('g', 'S1')])
data = np.loadtxt('./whData.dat', dtype=dt, comments='#', delimiter=None)

ws = data['w']
hs = data['h']
gs = np.array([el.decode('utf-8') for el in data['g']])

hs_t = hs[np.where(ws < 0)]
gs_t = gs[np.where(ws < 0)]
ws_t = ws[np.where(ws < 0)]

hs = np.delete(hs, np.where(ws < 0), None)
gs = np.delete(gs, np.where(ws < 0), None)
ws = np.delete(ws, np.where(ws < 0), None)

h_mean, h_std, h_var = np.mean(hs), np.std(hs), np.var(hs)
print h_mean, h_std, h_var
w_mean, w_std, w_var = np.mean(ws), np.std(ws), np.var(ws)
print w_mean, w_std, w_var

correlation_h_w = np.linalg.det(np.cov(hs, ws) / (h_std * w_std))
print correlation_h_w

#  p(x, y) -> p(h, w)
joint_mean = np.array([h_mean, w_mean])
joint_cov = np.mat([[h_var, correlation_h_w * h_std * w_std], [correlation_h_w * h_std * w_std, w_var]])
x, y = np.mgrid[155:195:0.5, 40:110:0.5]
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x
pos[:, :, 1] = y
rv = multivariate_normal.pdf(pos, joint_mean, joint_cov)
ax2.contour(x, y, rv)
X = np.vstack((hs, ws))
ax2.plot(X[0, :], X[1, :], 'ro', label='data')

leg = ax2.legend(loc='upper left', shadow=True, fancybox=True, numpoints=1)
leg.get_frame().set_alpha(0.5)
plt.show()
