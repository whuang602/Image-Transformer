from ast import increment_lineno
import os
import math

import numpy as np
import numpy.linalg as npla

import scipy
from scipy import sparse
from scipy import linalg
import scipy.sparse.linalg as spla

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
# %matplotlib tk

def compress(factor):
    # any image can input here to compress by the parameter factor
    image = plt.imread('image.jpg')
    img_Matrix = np.float64(image[:,:,0])
    rows, cols = img_Matrix.shape
    
    og_storage = rows * cols
    desired_storage = og_storage / factor
    k = desired_storage / (rows+cols)
    compressed_image = np.zeros(img_Matrix.shape)
    U,sigma,V = npla.svd(img_Matrix)
    for i in range(int(round(k))):
        compressed_image += sigma[i] * np.outer(U[:,i],V[i,:])
    compressed_rank = npla.matrix_rank(compressed_image)
    og_rank = npla.matrix_rank(img_Matrix)
    
    print('relative error:', sigma[round(k)]/sigma[0])
    print("Old Storage:", og_storage)
    plt.figure(figsize=(10,10))
    plt.gray()
    plt.imshow(img_Matrix)
    plt.title('original image')
    
    print("New Storage:",desired_storage)
    plt.figure(figsize=(10,10))
    plt.gray()
    plt.imshow(compressed_image)
    plt.title('compressed image (factor = %f)' % factor)
    
    return k,compressed_rank, og_rank