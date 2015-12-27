import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal, norm

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

h_mean, h_std = norm.fit(hs)
w_mean, w_std = norm.fit(ws)

#  p(x, y) -> p(h, w)
joint_mean = np.array([h_mean, w_mean])
cov_h_w = np.linalg.det(np.cov(hs, ws))
print cov_h_w
joint_cov = np.mat([[np.power(h_std, 2), cov_h_w], [cov_h_w, np.power(w_std, 2)]])
print joint_cov
fig = plt.figure()
ax = fig.add_subplot(111)
pos = np.dstack((hs, ws))
rv = multivariate_normal.pdf(pos, joint_mean, joint_cov)
#ax.contourf(hs, ws, rv)
plt.plot(rv)
plt.show()
