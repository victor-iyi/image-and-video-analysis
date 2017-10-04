"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 15 September, 2017 @ 5:44 AM.
  Copyright © 2017. Victor. All rights reserved.
"""

import cv2


def webcam(source=0, title="webcam"):
    """
    Make use of the system's webcam.

    :param source:
            Video stream source, if it's a number, the n webcam will be used.
            If it's a stream, it will assume a video source.
    :param title:
            Title to be written on the webcam window.
    """
    capture = cv2.VideoCapture(source)
    status, img = capture.read()

    print('Press <SPACE> to exit...')

    while status:
        status, img = capture.read()
        cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    webcam()
