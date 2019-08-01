% Depth Estimation using Optical Flow (disparity), Baseline (distance
% between stereo cameras, Focal Length (distance between object and image)

%% Load stereoParamsRect, add readFlowFile path, calculate baseline and focalLength

clc;
clear;

%stereo parameters of rectified frames
load('C:\Users\josep\OneDrive\Documents\Research\Assignment 5 Calibration_Rectification\stereoParamsRect');
%access readFlowFile function
addpath(genpath('C:\Users\josep\OneDrive\Documents\Research\Assignment 6 Depth_Optical_Flow_Merge\MATLAB\'));
%optical flow of rectified frames
addpath(genpath('C:\Users\josep\OneDrive\Documents\Research\Assignment 6 Depth_Optical_Flow_Merge\left_data_0409\left_rect_flow\'));
%rectified frames
addpath(genpath('C:\Users\josep\OneDrive\Documents\Research\Assignment 6 Depth_Optical_Flow_Merge\left_data_0409\left_rect_rgb\'));

baseline = abs(stereoParamsRect.TranslationOfCamera2(1));
focalLength = stereoParamsRect.CameraParameters1.FocalLength(1); %only choosing 1 right now

%% Calculate Depth

figure(1);

for frameIndex=2000:3000
    %load optical flow
    filename_flow = sprintf('%05d.flo',frameIndex);
    optFlow = readFlowFile(filename_flow);
    optFlowX = optFlow(:,:,1);
    optFlowY = optFlow(:,:,2);
    %resize optFlow to match rgb (if needed)
    optFlowX = optFlowX.*(592/512); %width_flow/width_rgb
    optFlowY = optFlowY.*(437/384); %height_flow/height_rgb
    optFlowX = imresize(optFlowX, [437 592]);
    optFlowY = imresize(optFlowY, [437 592]);
    %calculate depth
    depth = abs((baseline*focalLength)./optFlowX); %D=bf/d
    disparity = 1./depth;
    %save depth
    fullFilename = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_flow_depth\\cam_left_flow-depth_frame_%05d.mat',frameIndex);
    save(fullFilename,'depth');
    %frame
    filename_frame = sprintf('cam_left_rgb_frame_%05d.png',frameIndex);
    frame = imread(filename_frame);
    %plot
    subplot(2,1,1);
    imshow(disparity,[]);
    pause(0.001);
    subplot(2,1,2);
    imshow(frame,[]);
end

