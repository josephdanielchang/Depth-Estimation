#Input: numpy depth array, numpy scaled camera frames array
#Output: display disparity map and camera frames

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

depth_output = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_scaled\model-190532.npy')
frames = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_scaled\scaled_raw_data.npy')

disp_output = 1./depth_output
(z,h,w) = (depth_output.shape)                                  #2010x128x416
(r,s,t,u) = (frames.shape)                                      #2010x128x416x3
print(disp_output.shape)

fig, (ax1,ax2) = plt.subplots(2,1)
#fig = plt.plot()

for i in range(z):                                              #image index to display
    
    print(i+1)
    #concat = np.concatenate((frames[i], disp_output[i]), axis=1)
    #plt.imshow(concat)
    ax1 = plt.subplot("211").imshow(frames[i])                  #128x1248x3
    ax2 = plt.subplot("212").imshow(disp_output[i],cmap='gray')
    plt.pause(0.001)
    plt.clf()

