"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 20 September, 2017 @ 3:52 PM.
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2


def binary(img, minval, maxval, thresh_type=cv2.THRESH_BINARY, grayscale=True, display=False):
    if grayscale:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img, minval, maxval, thresh_type)
    if display:
        cv2.imshow('Binary Threshold', img_thresh)
    return img_thresh


def adaptive(img, maxval, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresh_type=cv2.THRESH_BINARY, block_size=13, C=19, display=False):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.adaptiveThreshold(img, maxval, method, thresh_type, block_size, C)
    if display:
        cv2.imshow('Adaptive Threshold', img_thresh)
    return img_thresh


def main():
    img = cv2.imread('../data/images/3.jpg')
    cv2.imshow('Original', img)
    # Binary threshold
    binary(img, 150, 255, grayscale=False, display=True)
    # Adaptive threshold
    adaptive(img, 255, display=True)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
