#Input: numpy depth array, camera frames
#Output: display disparity map and camera frames

#disp_tf            |    <class 'numpy.float32'>    |    (2010, 128, 416)

import numpy as np
import matplotlib.pyplot as plt
import cv2

### SETUP DISP_TF ###
depth_tf = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\5G Forum Demo\05-21-19_Nissan_left_output_1000\model-190532.npy')
frames = np.load(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\5G Forum Demo\05-21-19_Nissan_left_output_1000\scaled_raw_data.npy')
s = 1       #CHANGE: starting index
z = 1000    #CHANGE: number of frames

for i in range(z):

    print(i)

    disp_tf = 1./depth_tf[i]
    disp_tf = cv2.resize(disp_tf, dsize=(640, 480))
    framesResize = cv2.resize(frames[i], dsize=(640, 480))
    
    ### SAVE FRAMES, DISP AS PNG ###
    plt.imsave(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\5G Forum Demo\05-21-19_Nissan_left_output_1000\scaled_rgb\cam_left_rgb_%05i.png' %(s+i), framesResize, cmap='gray')
    plt.imsave(r'C:\Users\josep\OneDrive\Documents\Research\Assignment 4 Depth_Estimation\5G Forum Demo\05-21-19_Nissan_left_output_1000\disp\cam_left_depth_%05i.png' %(s+i), disp_tf, cmap='gray')

    plt.pause(0.001)
