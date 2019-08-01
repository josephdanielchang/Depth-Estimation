#Input: numpy depth array, camera frames
#Output: display disparity map and camera frames

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

depth_output = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_unscaled\model-190532.npy')
disp_output = 1./depth_output
(z,h,w) = (depth_output.shape)                                  #2010x128x416

fig, (ax1,ax2) = plt.subplots(2,1)

for i in range(z):                                              #image index to display

    frame = Image.open(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\raw_data\cam_1_1\cam_1_1_trim_zoom_1\cam_1_1_trim %04i.jpg' %(i+1)) 
    print(i+1)
    ax1 = plt.subplot("211").imshow(frame)                      #128x1248x3
    ax2 = plt.subplot("212").imshow(disp_output[i],cmap='gray')
    plt.pause(0.001)
    plt.clf()
