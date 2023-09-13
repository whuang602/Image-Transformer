from ast import increment_lineno

import numpy as np

import matplotlib.pyplot as plt

# Rotates a square image clockwise
def rotate(filename:str, times:int)->bool:

    print("\n     Begin Rotate...")
    # imread -> pillow -> bytestring is built and thus immutable, requires copying to make mutable version
    image = plt.imread(filename).copy()
    img_Matrix = np.float64(image[:,:,0])
    rows, cols = img_Matrix.shape

    if rows == 1 or cols == 1:
        return True
    
    if rows != cols:
        if input("\n     Warning: uploaded image is not a square, continue(y/n)? ") != "y":
            return False
            
    array = [[] for i in range(4)]
    for time in range(int(times)):
        for i in range(int(rows/2)):
            for j in range(int(rows-2*i-1)):
                # .flatten is required as image[x][y] is ndarray and is accessed abnormally
                array[0].append(image[i][i+j].flatten())

                array[1].append(image[i+j][rows-1-i].flatten())
                image[j+i][rows-1-i] = array[0][-1]

                array[2].append(image[rows-1-i][rows-1-i-j].flatten())
                image[rows-1-i][rows-1-i-j] = array[1][-1]
                
                array[3].append(image[rows-1-i-j][i].flatten())
                image[rows-1-i-j][i] = array[2][-1]

                image[i][i+j] = array[3][-1]
                # plt.imshow(image, interpolation='nearest')
                # plt.savefig('images/iteration_'+str(0)+"_"+str(i)+'.png', transparent= True, bbox_inches='tight', pad_inches=0)

    plt.imsave(filename[:-4]+'_rotated'+filename[-4:],image)
        
    print("\n     Rotation complete! New image stored as: "+filename[:-4]+'_rotated'+filename[-4:])
    return True
