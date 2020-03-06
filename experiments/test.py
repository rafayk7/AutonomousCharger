from vision import CircleLib, ArucoLib

test = ArucoLib(calibration_file="mac_webcam_camera_config.pkl", save_path="circledata/thresh")

test.do_video()
# test.add_image("with_flash.jpg")
# test.shape_detect()


