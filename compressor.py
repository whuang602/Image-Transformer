from ast import increment_lineno
# import os
# import math

import numpy as np
import numpy.linalg as npla

# import scipy
# from scipy import sparse
# from scipy import linalg
# import scipy.sparse.linalg as spla

import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import axes3d
# %matplotlib tk

def compress(filename:str, factor:int)->bool:
    if input("\n     Warning: compression will turn the image into grayscale, continue(y/s)? ") != "y":
        return False
    # any image can input here to compress by the parameter factor
    image = plt.imread(filename).copy()
    img_Matrix = np.float64(image[:,:,0])
    rows, cols = img_Matrix.shape
    
    og_storage = rows * cols
    desired_storage = og_storage / factor
    k = desired_storage / (rows+cols)
    compressed_image = np.zeros((rows,cols))
    U,sigma,V = npla.svd(img_Matrix)
    for i in range(int(round(k))):
        compressed_image += sigma[i] * np.outer(U[:,i],V[i,:])
    # compressed_rank = npla.matrix_rank(compressed_image)
    # og_rank = npla.matrix_rank(img_Matrix)
    
    # print('relative error:', sigma[round(k)]/sigma[0])
    # print("Old Storage:", og_storage)
    # print("New Storage:",desired_storage)
    plt.gray()
    plt.imsave(filename[:-4]+'_compressed'+filename[-4:],compressed_image) # using savefig saves as a figure and enforces unnecessary pixel loss
        
    print("\n     Compression complete! New image stored as: "+filename[:-4]+'_compressed'+filename[-4:]) 
    
    # return k,compressed_rank, og_rank
    return True