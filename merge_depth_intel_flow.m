% Merge depth from Intel RealSense cameras and geometric optical flow

clc;
clear;

%%

figure(1);

for frameIndex=2000:3000
    %load rectified intel depth
    
    fullFilename = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_intel_depth\\cam_left_depth_frame_%05d.png',frameIndex);
    intel_depth = imread(fullFilename);
    %load rectified optical flow depth
    fullFilename = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_flow_depth\\cam_left_flow-depth_frame_%05d.mat',frameIndex);
    flow_depth = load(fullFilename);
    flow_depth = flow_depth.depth;
    flow_depth = uint16(flow_depth);
    
    %merge depth
    merge_depth = intel_depth;      
    %replace intel depth zeros with flow depth
    t = merge_depth == 0;
    merge_depth(t) = flow_depth(t);
    %replace intel depth nonzeros with flow depth and intel depth mean
    t = ~t;
    merge_depth(t) = (intel_depth(t)+flow_depth(t))./2;
    
    %display merged_depth, rect_rgb
%     filename_frame = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_rgb\\cam_left_rgb_frame_%05d.png',frameIndex);
%     frame = imread(filename_frame);
%     subplot(2,1,1);
%     imshow(merge_depth,[]);
%     pause(0.001);
%     subplot(2,1,2);
%     imshow(frame,[]);
    
    %display intel_depth,flow_depth,merged_depth,rect_rgb
    filename_frame = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_rgb\\cam_left_rgb_frame_%05d.png',frameIndex);
    subplot(2,2,1);
    imshow(flow_depth,[]);
    subplot(2,2,2);
    imshow(intel_depth,[]);
    frame = imread(filename_frame);
    subplot(2,2,3);
    imshow(merge_depth,[]);
    pause(0.001);
    subplot(2,2,4);
    imshow(frame,[]);
    
    %save merged depth
    %fullFilename = sprintf('C:\\Users\\josep\\OneDrive\\Documents\\Research\\Assignment 6 Depth_Optical_Flow_Merge\\left_data_0409\\left_rect_merge_depth\\cam_left_merge_frame_%05d.png',frameIndex);
    %imwrite(merge_depth,fullFilename)
end











