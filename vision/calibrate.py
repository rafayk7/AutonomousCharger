import numpy as np
import cv2
import glob
import sys
import pickle
import os
import matplotlib.pyplot as plt


def save_images():
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("calibration/data/{}.jpg".format(count), img)

        count += 1
        # Display the resulting frame
        plt.imshow(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Saved all images")
    return

def get_camera_config(path_to_images):
    images = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path_to_images):
        for file in f:
            if '.jpg' in file or '.jpeg' in file:
                images.append(os.path.join(r, file))

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    count = 0
    for image in images:
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(img, (7, 6), None)

        # If found, add object points, image points (after refining them)
        if ret:
            count += 1
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
            cv2.imwrite("calibration/processed/{}.jpg".format(count), img)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-1],None,None)

    with open('mac_webcam_camera_config.pkl', 'wb') as f:
        pickle.dump((mtx, dist), f)
        print("Configuration saved.")

    return

def main():
    get_camera_config("calibration/data")

main()

#
# # termination criteria
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#
# # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((6*7,3), np.float32)
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
#
# # Arrays to store object points and image points from all the images.
# objpoints = [] # 3d point in real world space
# imgpoints = [] # 2d points in image plane.
#
#
# cap = cv2.VideoCapture(0)
#
#
# for i in range(1):
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert to grayscale
#
#
#     # Find the chess board corners
#     ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
#     cv2.imshow('img',img)
#     cv2.waitKey(1000)
#
#     # If found, add object points, image points (after refining them)
#     if ret:
#         objpoints.append(objp)
#
#         corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
#         imgpoints.append(corners2)
#
#         # Draw and display the corners
#         img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
#         cv2.imshow('img',img)
#         cv2.waitKey(1000)
#
#     cv2.imshow('img',img)
#     cv2.waitKey(1000)
#
# cap.release()
# cv2.destroyAllWindows()
#
# with open('workfile.pckl','wb') as f:
#     ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
#     pickle.dump((mtx,dist),f)
#
#     # Re-projection errors
# tot_error = 0
# mean_error = 0
# for i in range(len(objpoints)):
#     imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
#     error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
#     tot_error += error
#
# print ("total error: ", mean_error/len(objpoints))
