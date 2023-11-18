import math
from pupil_apriltags import Detector
from map import *
import numpy as np
import cv2

global_results = []

def calc_dist(focal_length, tag_size, pixel_size):
    return (tag_size * focal_length) / pixel_size


def main():
    global global_results 

    cap = cv2.VideoCapture(0)
    detector = Detector(families='tag16h5', quad_sigma=0.8)
    tag_size = 0.16
    focal_length = 1000
    c_params = [focal_length, focal_length, 1280 / 2, 720 / 2]
    map = Map()
    map.set_tag(6, 0, 0, 0)

    while True:
        ret, frame = cap.read() 
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = detector.detect(gray, estimate_tag_pose=True, camera_params=tuple(c_params), tag_size=tag_size)
        for tag in tags:
            if tag.decision_margin > 15:
                tag_id = tag.tag_id
                corners = tag.corners

                pixel_size = np.linalg.norm(corners[0] - corners[1])
                dist = calc_dist(focal_length, tag_size, pixel_size)
                print("Tag ID: {}, Distance: {}, Orientation: {}, Translation: {}".format(tag_id, dist, tag.pose_R,
                                                                                          tag.pose_t))
                # map.get_position([tag_id], [tag.pose_R, tag.pose_t])
                for corner in corners:
                    cv2.circle(frame, tuple(corner.astype(int)), 5, (0, 0, 255), -1)

                cv2.putText(frame, str(tag_id), tuple(corners[0].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                            2)
                cv2.putText(frame, str(round(dist, 2)), tuple(corners[1].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)
                rot = rotation_matrix_to_euler_angles(tag.pose_R)
                t_round = np.round(tag.pose_t, 2)
                rot_rounded = [round(i, 2) for i in rot]
                cv2.putText(frame, str(rot_rounded), tuple(corners[3].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(frame, str(t_round), tuple(corners[2].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                global_results.append((dist, rot, t_round))

        cv2.imshow('AprilTags', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def rotation_matrix_to_euler_angles(R):
    r11, r12, r13 = R[0, 0], R[0, 1], R[0, 2]
    r21, r22, r23 = R[1, 0], R[1, 1], R[1, 2]
    r31, r32, r33 = R[2, 0], R[2, 1], R[2, 2]

    pitch = math.atan2(-r23, math.sqrt(r11 ** 2 + r13 ** 2))

    yaw = math.atan2(r21, r22)

    roll = math.atan2(r13, r33)

    pitch = math.degrees(pitch)
    yaw = math.degrees(yaw)
    roll = math.degrees(roll)

    return [roll, pitch, yaw]


if __name__ == "__main__":
    main()
    print(global_results)  # Print the global results variable
