"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 14 September, 2017 @ 3:21 PM.
  Copyright © 2017. Victor. All rights reserved.
"""

import cv2


def main():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
