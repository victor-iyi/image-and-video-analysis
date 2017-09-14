"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 14 September, 2017 @ 5:18 PM.
  Copyright © 2017. Victor. All rights reserved.
"""

import os.path
import cv2

""" Preset Colors """
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# BGR
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
# CYMK
CYAN = ()
MAGENTA = ()
YELLOW = ()

""" Preset thickness """
THICKNESS_THIN = 1
THICKNESS_THICK = 3

""" Preset fonts """
FONT_ITALIC = cv2.FONT_ITALIC
FONT_HERSHEY_PLAIN = cv2.FONT_HERSHEY_PLAIN
FONT_HERSHEY_COMPLEX = cv2.FONT_HERSHEY_COMPLEX
FONT_HERSHEY_COMPLEX_SMALL = cv2.FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_SCRIPT_COMPLEX = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
FONT_HERSHEY_SCRIPT_SIMPLEX = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SIMPLEX = cv2.FONT_HERSHEY_SIMPLEX
FONT_HERSHEY_DUPLEX = cv2.FONT_HERSHEY_DUPLEX
FONT_HERSHEY_TRIPLEX = cv2.FONT_HERSHEY_TRIPLEX


def line(img, pt1, pt2, color=GREEN, thickness=THICKNESS_THIN, **kwargs):
    cv2.line(img, pt1, pt2, color, thickness, **kwargs)


def rectangle(img, pt1, pt2, color=GREEN, thickness=THICKNESS_THIN, **kwargs):
    cv2.rectangle(img, pt1, pt2, color, thickness, **kwargs)


def poly(img, pts, isClosed, color=GREEN, thickness=THICKNESS_THIN, **kwargs):
    cv2.polylines(img, pts, isClosed, color, thickness, **kwargs)


def text(img, text, org, fontFace=FONT_HERSHEY_PLAIN, fontScale=5, color=BLUE, thickness=THICKNESS_THICK, **kwargs):
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, **kwargs)


def start():
    image_dir = "../data/images"
    filename = os.path.join(image_dir, "3.jpg")

    img = cv2.imread(filename)

    line(img, (0, 0), (100, 100), RED, THICKNESS_THICK)
    rectangle(img, (100, 100), (350, 350), GREEN, THICKNESS_THICK)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start()
