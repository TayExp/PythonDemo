import matplotlib.pyplot as plt
import numpy as np
# Load models
#
# t = np.linspace(0,0.1,6)
# in21 = np.transpose(np.asarray([[0, 0, 288.1, 0, 0, 0, 1]]*6))
# in22 = [0.00533373443544054,  0.0265567984975557,0.0686686176048889, 0.131226939306055,0.213794735821576,0.315940180234382]
# in1 = np.transpose(np.asarray([[0,-25,30,0]]*6))
# u_traj = np.transpose(np.vstack((t,in21,in22,in1)))
#
#
# np.savetxt('u.txt',u_traj)

d = np.loadtxt(fname='u.txt')

print(d)