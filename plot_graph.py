import matplotlib.pyplot as plt
import scipy.io
import numpy as np
#from scipy.stats import norm
import random
from datetime import datetime

from numpy.linalg import det, norm


from mpl_toolkits import mplot3d
import sys





MAT_FILE = sys.argv[1]
LABEL_FILE = sys.argv[2]

data_mat = scipy.io.loadmat(MAT_FILE)#'Data.mat')
test = np.array(data_mat['X'])



# load numpy array from npz file
from numpy import load
# load dict of arrays
dict_data = load(LABEL_FILE)#'classification.npz')
# extract the first array
classification = dict_data['arr_0']
# print the array
print(classification)

random.seed(datetime.now())

colors = [(random.random(), random.random(), random.random()) for i in range(0,max(classification)+1)]#['red','blue','green','yellow','black','white',]

plt_colors = [colors[i] for i in classification]




fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
ax = plt.axes(projection='3d')
ax.scatter3D(test[0,:],test[1,:],test[2,:],c=plt_colors)
#ax.scatter(test[0,:],test[1,:],test[2,:],c=plt_colors)

plt.show()

