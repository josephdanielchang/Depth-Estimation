#Input: numpy depth array, camera frames
#Output: display disparity map and camera frames

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

frames = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_scaled\scaled_raw_data.npy')
z = 2010    #CHANGE: number of frames

fig, (ax1,ax2) = plt.subplots(2,1)

for i in range(z):                                              #image index to display

    print(i+1)
    depth_output = Image.open(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou-PyTorch\Output\cam_1_1_trim_1\-cam_1_1_trim %04i_depth.jpg' %(i+1))
    depth_numpy = np.array(depth_output)                        #128x416x3
    disp_numpy = 1./depth_numpy
    ax1 = plt.subplot("211").imshow(frames[i])
    disp_numpy = disp_numpy[:,:,1] - disp_numpy[:,:,2]
    ax2 = plt.subplot("212").imshow(disp_numpy,cmap='gray')
    plt.pause(0.001)
    plt.clf()
