from vision import ArucoLib, CircleLib

class Control:
    def __init__(self):
        self.img = None
        self.current_vision = ArucoLib()

    def control(self):
        self.current_vision.add_image(self.img)

    # def get_angle_from_coordinate(self, x, y, z, yaw):
        #

def main():
    aruco_lib = ArucoLib(calibration_file="mac_webcam_camera_config.pkl", save_path="data/4x4")
    aruco_lib.do_video()

main()