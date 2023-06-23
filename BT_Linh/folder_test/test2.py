import argparse
import os
from os.path import join as opj
import time
from datetime import datetime
import time

import cv2
import numpy as np

parser = argparse.ArgumentParser(description="Streaming webcam",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--device", type=int, default=0, help="device id")

font = cv2.FONT_HERSHEY_SIMPLEX

def create_folder():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("Date_%d_%m_%Y_Time_%H_%M_%S")
    os.makedirs(current_time, exist_ok=True)
    return current_time


def main(device):
    folder_path = create_folder()
    new_frametime = 0
    prev_frametime = 0
    vid = cv2.VideoCapture(device)
    frame_count = 0
    while(True):
        # Capture the video frame
        # by frame
        ret, ori_image = vid.read()
        frame_count += 1
        # Display the resulting frame
        if not ret:
            continue
        frame = ori_image.copy()
        new_frametime = time.time()
        frametime = new_frametime - prev_frametime
        fps = 'FPS: {}'.format(str(int(1/frametime)))
        prev_frametime = new_frametime
        frametime *= 1000
        delay_str = 'Delay: {}ms'.format(int(frametime))
        cv2.putText(
            frame, fps, (7, 30), font, 1, (0, 0, 139), 2, cv2.LINE_AA
        )
        cv2.putText(
            frame, delay_str, (200, 30), font, 1, (0, 0, 139), 2, cv2.LINE_AA
        )
        cv2.imshow('frame', frame)
        image_name = 'frame_{}.jpg'.format(frame_count)
        cv2.imwrite(opj(folder_path, image_name), ori_image)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.device)