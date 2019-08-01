% rename file name
% start index from one

clear;close all;clc;

image_dir = dir('C:/Users/josep/OneDrive/Documents/Research/Assignment 7 Vehicle_Collaboration/nissan_images/walk/cam_left_60064/depth/*.png'); %accord left images

for idx = 1:1000
%for idx = 1
    img = imread(sprintf('%s/%s',image_dir(idx).folder, image_dir(idx).name));
    %Custom output file name
    imwrite(img,sprintf('C:/Users/josep/OneDrive/Documents/Research/Assignment 7 Vehicle_Collaboration/nissan_images/walk/cam_left_60064/depth_renamed/cam_nissan_left_depth_%05i.png', idx));
end
