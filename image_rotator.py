from ast import increment_lineno
# import os
# import math

import numpy as np
# import numpy.linalg as npla

import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import axes3d

# convert rectangular image to square (Incomplete)
# What it does: select the center of the image and crop it
def squarify(image:np.ndarray, rows:int, cols:int)->bool:
    if rows==cols:
        print("Already a square")
        return False

    difference = abs(cols-rows)

    if cols > rows: # longer
        print()
    else: # taller
        print()
    return True


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
        if input("Warning: uploaded image is not a square, continue(y/n)? ") != "y":
            return False
        # if input("Do you want to convert it to a square(y/n)? (original image unaffected) ") == "y":
        #     squarify(image, rows, cols)
            
        
    resolution = cols/float(200),rows/float(200)
    plt.figure(figsize=resolution)
    plt.axis('off')
    plt.imshow(image, interpolation='nearest')
    plt.margins(0,0)
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

    plt.imshow(image, interpolation='nearest')
    plt.savefig(filename[:-4]+'_edited.png', transparent= True, bbox_inches='tight', pad_inches=0)
        
    print("\n     Rotation complete! New image stored as: "+filename[:-4]+'_edited.png')
    return True

print("----------------------- Editor program starting -----------------------\n")
filename = input("     What file would you like to edit? (.png, .jpg, etc) ")
request = input("\n     What would you like to do? (R: rotate clockwise, C: compress) ")
while request in ["R", "C"]:
    match (request):
        case "R":
            rotate(filename, int(input("\n     How many times would you like to rotate the image? ")))
        case "C":
            print("Compressor not yet linked")
    request = input("\n     What would you like to do? (R: rotate clockwise, C: compress) ")
print("------------------------- Exiting editor -------------------------")
