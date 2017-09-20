"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 20 September, 2017 @ 3:52 PM.
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2


def binary(img, minval, maxval, grayscale=True):
    if grayscale:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, image_thresh = cv2.threshold(img, minval, maxval, cv2.THRESH_BINARY)
    return image_thresh


if __name__ == '__main__':
    img = cv2.imread('../data/images/5.jpg')
    img = binary(img, 12, 255)

    cv2.imshow('Binary threshold', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
