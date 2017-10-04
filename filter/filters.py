"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 04 October, 2017 @ 12:35 AM.
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2
import numpy as np


def color(img, lower_bound, upper_bound):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_bound = np.array(lower_bound)
    upper_bound = np.array(upper_bound)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    img_filter = cv2.bitwise_and(img, img, mask=mask)
    return img_filter


def blur(img):
    pass


def __webcam():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        # Applying color filtering
        color_filter = color(frame, [0, 0, 0], [255, 255, 255])
        cv2.imshow('Color Filter', color_filter)
        # Applying blur

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    __webcam()


if __name__ == '__main__':
    main()
