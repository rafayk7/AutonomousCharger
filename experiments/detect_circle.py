import cv2
import numpy as np

path_full_zoom = "with_flash.jpg"


def hough_detect():
    def draw_circles(circles, output):
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)



    img = cv2.imread(path_full_zoom)
    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))
    thresh = cv2.threshold(gray_blurred, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    edged = cv2.Canny(thresh, 100, 200)
    circles = cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, 1,20,
                                param1=50,param2=72,minRadius=0,maxRadius=0)
    draw_circles(circles, img)
    cv2.imwrite("detected.jpg", img)

def blob_detect():
    im = cv2.imread(path_full_zoom)
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("detected_blob.jpg", im_with_keypoints)

blob_detect()

# # Apply Hough transform on the blurred image.
# detected_circles = cv2.HoughCircles(thresh,
#                                     cv2.HOUGH_GRADIENT, 1, 60, param1=200,
#                                     param2=30, minRadius=1, maxRadius=40)


# # Draw circles that are detected.
# if detected_circles is not None:
#
#     # Convert the circle parameters a, b and r to integers.
#     detected_circles = np.uint16(np.around(detected_circles))
#
#     for pt in detected_circles[0, :]:
#         a, b, r = pt[0], pt[1], pt[2]
#
#         # Draw the circumference of the circle.
#         cv2.circle(img, (a, b), r, (0, 255, 0), 2)
#
#         # Draw a small circle (of radius 1) to show the center.
#         cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
#         cv2.imwrite("test.jpg", img)
