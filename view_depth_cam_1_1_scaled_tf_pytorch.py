#Input: numpy depth array, camera frames
#Output: display disparity map and camera frames

#disp_tf            |    <class 'numpy.float32'>    |    (2010, 128, 416)
#depth_pt_numpy     |    <class 'numpy.uint8'>      |    (128, 416, 3)
#disp_pt_numpy      |    <class 'numpy.float64'>    |    (128, 416, 3)

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

### SETUP DISP_TF ###
depth_tf = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_scaled\model-190532.npy')
frames = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou\Output\depth_output_test\cam_1_1_trim_zoom_1_scaled\scaled_raw_data.npy')
disp_tf = 1./depth_tf
z = 2010    #CHANGE: number of frames
fig, (ax1,ax2,ax3) = plt.subplots(3,1)

for i in range(z):

    print(i+1)

    ### SETUP DISP_PT_NUMPY ###
    depth_pt = Image.open(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou-PyTorch\Output\cam_1_1_trim_1_depth\-cam_1_1_trim %04i_depth.jpg' %(i+1))
    disp_pt = Image.open(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\Zhou-PyTorch\Output\cam_1_1_trim_1_disp\-cam_1_1_trim %04i_disp.jpg' %(i+1))
    depth_pt_numpy = np.array(depth_pt)
    disp_pt_numpy = 1/(np.array(depth_pt))
    
    ### PLOT FRAMES, DISP ###
    ax1 = plt.subplot("311").imshow(frames[i])
    ax2 = plt.subplot("312").imshow(disp_tf[i], cmap='gray')
    ax3 = plt.subplot("313").imshow(disp_pt_numpy[:,:,2], cmap='gray')
    #ax3 = plt.subplot("313").imshow(disp_pt[:,:,0], cmap='gray')

    ### VIEW DEPTH VALUES ###
    print('DEPTH_TENSORFLOW\n')
    print(depth_tf[i,108:128,396:416])
    #print(depth_tf[i])
    print('DEPTH_PYTORCH\n')
    print(depth_pt_numpy[108:128,396:416,1])
    #print(depth_pt_numpy[:,:,1])

    plt.pause(0.001)
    plt.clf()
