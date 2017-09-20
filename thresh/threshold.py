"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 20 September, 2017 @ 3:52 PM.
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2


def binary(img, minval, maxval):
    cv2.threshold(img, minval, maxval, cv2.THRESH_BINARY)


if __name__ == '__main__':
    img = cv2.imread('../data/images/3.jpg')
    binary(img, 12, 255)
