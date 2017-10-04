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
    """
    Color filtering

    :param img: image to be filtered.
    :param lower_bound: inclusive lower boundary array or a scalar.
    :param upper_bound: inclusive upper boundary array or a scalar.
    :return: A filtered image.
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # upper and lower bound
    lower_bound = np.array(lower_bound)
    upper_bound = np.array(upper_bound)
    # mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    # filter the image
    img_filter = cv2.bitwise_and(img, img, mask=mask)
    return img_filter


def blur(img, size, depth=-1, blur_type=None):
    """
    Blurring filters.

    :param img:
            Image to be blurred.
    :param size:
            The blur size. A higher number will have a low clarity.
            A lower number will be clearer.
    :param depth:
    :param blur_type:
    :return:
    """
    blur_type = str(blur_type).lower if blur_type else blur_type
    if blur_type == 'gaussian':
        blurred = cv2.GaussianBlur(img, (size, size), depth)
    elif blur_type == 'median':
        blurred = cv2.medianBlur(img, size)
    elif blur_type == 'bilateral':
        blurred = cv2.bilateralFilter(img, depth, size, size)
    else:
        kernel = np.ones(shape=[size, size], dtype=np.float32) / (size * size)
        blurred = cv2.filter2D(img, depth, kernel)

    return blurred


def __webcam():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        # Apply transformations
        color_filter = color(frame, [100, 50, 50], [200, 200, 200])
        blurred = blur(frame, size=15, blur_type='gaussian')
        # Displaying
        cv2.imshow('Color Filter', color_filter)
        cv2.imshow('Blurred', blurred)
        # Exiting the window
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    __webcam()


if __name__ == '__main__':
    main()
