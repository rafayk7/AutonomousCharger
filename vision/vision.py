import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import pickle
import os
import imutils

class VisionClass:
	def __init__(self, calibration_file, save_path):
		self.img = None
		self.save_path = save_path
		self.help_statement = None

		self.X = None
		self.Y = None
		self.Z = None

		self.Yaw = None
		self.Pitch = None
		self.Roll = None

		self.camera_matrix = None
		self.camera_distortion = None

		with open(calibration_file, 'rb+') as f:
			self.camera_matrix, self.camera_distortion = pickle.load(f)



	def add_image(self, image_path):
		self.img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
		print("{} added.".format(image_path))

		return

	def add_save_path(self, save_path):
		self.save_path = save_path
		print("Save path updated to {}.".format(save_path))

	def display_data(self, clear = False):
		print("X : {}".format(self.X))
		print("Y : {}".format(self.Y))
		print("Z : {}".format(self.Z))

		print("Yaw: {}".format(self.Yaw))
		print("Pitch: {}".format(self.Pitch))
		print("Roll: {}".format(self.Roll))

		if clear:
			os.system("clear")

		return

	def help(self):
		print(self.help_statement)

	def process(self):
		pass

	def do_video(self):
		cap = cv2.VideoCapture(0)

		while True:
			# Capture frame-by-frame
			ret, frame = cap.read()

			# Our operations on the frame come here
			self.img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			self.process()
			# Display the resulting frame
			cv2.imshow('frame',self.img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()

		return

class CircleLib(VisionClass):
	def __init__(self, calibration_file, save_path):
		super().__init__(calibration_file, save_path)

	def hough(self):
		circles = cv2.HoughCircles(self.img, cv2.HOUGH_GRADIENT, 1, 20,
								   param1=50, param2=30, minRadius=0, maxRadius=0)

		circles = np.uint16(np.around(circles))
		for i in circles[0, :]:
			# draw the outer circle
			cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
			# draw the center of the circle
			cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)


	def shape_detect(self):
		def detect(c):
			# initialize the shape name and approximate the contour
			shape = "unidentified"
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)

			# if the shape is a triangle, it will have 3 vertices
			if len(approx) == 3:
				shape = "triangle"
			# if the shape has 4 vertices, it is either a square or
			# a rectangle
			elif len(approx) == 4:
				# compute the bounding box of the contour and use the
				# bounding box to compute the aspect ratio
				(x, y, w, h) = cv2.boundingRect(approx)
				ar = w / float(h)
				# a square will have an aspect ratio that is approximately
				# equal to one, otherwise, the shape is a rectangle
				shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
			# if the shape is a pentagon, it will have 5 vertices
			elif len(approx) == 5:
				shape = "pentagon"
			# otherwise, we assume the shape is a circle
			else:
				shape = "circle"
			# return the name of the shape
			return shape

		resized = imutils.resize(self.img, width=300)
		ratio = self.img.shape[0] / float(resized.shape[0])

		thresh  = cv2.threshold(self.img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		# loop over the contours
		for c in cnts:
			# compute the center of the contour, then detect the name of the
			# shape using only the contour
			# M = cv2.moments(c)
			# cX = int((M["m10"] / M["m00"]) * ratio)
			# cY = int((M["m01"] / M["m00"]) * ratio)
			shape = detect(c)
			print("{} detected. BOX : {}".format(shape, cv2.boundingRect(c)))
			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")

		cimg = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)

		cv2.drawContours(cimg, cnts, -1, (0, 0, 255), 2)

		cv2.imwrite("{}/square_det.jpg".format(self.save_path), cimg)

	def test(self):
		(thresh, img_bin) = cv2.threshold(self.img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		img_bin = 255 - img_bin

		kernel_length = np.array(self.img).shape[1] // 80



		verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
		# A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
		hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
		# A kernel of (3 X 3) ones.
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

		img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
		verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
		cv2.imwrite("verticle_lines.jpg", verticle_lines_img)

		# Morphological operation to detect horizontal lines from an image
		img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
		horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
		cv2.imwrite("horizontal_lines.jpg", horizontal_lines_img)

		# Weighting parameters, this will decide the quantity of an image to be added to make a new image.
		alpha = 0.5
		beta = 1.0 - alpha
		# This function helps to add two image with specific weight parameter to get a third image as summation of two image.
		img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
		img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
		(thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		cv2.imwrite("img_final_bin.jpg", img_final_bin)

		# Find contours for image, which will detect all the boxes
		contours, h = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		cv2.drawContours(self.img, contours, -1, (0, 255, 0), 3)
		cv2.imwrite("{}/square_det.jpg".format(self.save_path), self.img)


	def find_squares(img):
		img = cv2.GaussianBlur(img, (5, 5), 0)
		squares = []
		for gray in cv2.split(img):
			for thrs in range(0, 255, 26):
				if thrs == 0:
					bin = cv2.Canny(gray, 0, 50, apertureSize=5)
					bin = cv2.dilate(bin, None)
				else:
					_retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
				bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
				for cnt in contours:
					cnt_len = cv2.arcLength(cnt, True)
					cnt = cv2.approxPolyDP(cnt, 0.02 * cnt_len, True)
					if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
						cnt = cnt.reshape(-1, 2)
						max_cos = np.max([angle_cos(cnt[i], cnt[(i + 1) % 4], cnt[(i + 2) % 4]) for i in range(4)])
						# print(cnt)
						a = (cnt[1][1] - cnt[0][1])

						if max_cos < 0.1 and a < img.shape[0] * 0.8:
							squares.append(cnt)
		return squares


class ArucoLib(VisionClass):
	def __init__(self, calibration_file, save_path):
		super().__init__(calibration_file, save_path)

		self.dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
		self.marker = None
		self.marker_id = None

		self.help_statement = "First, add an image. Then, get markers. Then, get pose."

	def create_aruco_markers(self):
		fig = plt.figure()
		nx = 4
		ny = 3
		for i in range(1, nx*ny+1):
			ax = fig.add_subplot(ny,nx, i)
			img = aruco.drawMarker(self.dict,i, 700)
			cv2.imwrite("{}/{}.jpg".format(self.save_path, i), img)
			plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
			ax.axis("off")

		plt.savefig("{}/markers.pdf".format(self.save_path ))
		plt.show()

	def get_markers(self):
		if self.img is None:
			print("Add an image before trying to get markers.")
			return

		ids = []
		corners = []

		corners, ids, _ = aruco.detectMarkers(self.img, self.dict)

		if ids:
			if len(ids) > 0:
				self.marker_id = ids[0]
				self.marker = [corners[0]]
				print("Marker with id {} detected.".format(self.marker_id))
		else:
			print("No marker detected.")

		return

	def get_pose(self):
		if self.marker is None:
			print("Get markers before getting pose.")
			return

		rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(self.marker, 0.056, self.camera_matrix, self.camera_distortion)

		rvecs = rvecs[0]
		tvecs = tvecs[0]

		eulerAngles = self.rvec_to_euler_angles(rvecs)

		self.X = tvecs.item(0)
		self.Y = tvecs.item(1)
		self.Z = tvecs.item(2)

		self.Yaw = eulerAngles[1]
		self.Pitch = eulerAngles[0]
		self.Roll = eulerAngles[2]

		return
	def rvec_to_euler_angles(self, rvec):
		mat, jac = cv2.Rodrigues(rvec)

		sy = np.sqrt(mat[0, 0] * mat[0, 0] + mat[1, 0] * mat[1, 0])

		singular = sy < 1e-6

		if not singular:
			x = np.math.atan2(mat[2, 1], mat[2, 2])
			y = np.math.atan2(-mat[2, 0], sy)
			z = np.math.atan2(mat[1, 0], mat[0, 0])

		else:
			x = np.math.atan2(-mat[1, 2], mat[1, 1])
			y = np.math.atan2(-mat[2, 0], sy)
			z = 0

		return np.array([x, y, z])

	def process(self, display=True):
		self.get_markers()
		self.get_pose()

		if display:
			self.display_data()

		return



