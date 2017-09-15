"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 15 September, 2017 @ 5:44 AM.
  Copyright © 2017. Victor. All rights reserved.
"""

import cv2


def read(filename, **kwargs):
    return cv2.imread(filename, **kwargs)


def show(title, img, size=None):
    img = img if size is None else cv2.resize(img, size)
    cv2.imshow(title, img)
    print("Press any key to exit")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = "../data/images/3.jpg"
    img = read(filename)
    show('img', img)
