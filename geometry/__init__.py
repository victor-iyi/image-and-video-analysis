"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 14 September, 2017 @ 5:18 PM.
  Copyright © 2017. Victor. All rights reserved.
"""

import os.path


def start():
    import geometry.shapes as shapes
    import load.image as image

    image_dir = "../data/images"
    filename = os.path.join(image_dir, "6.jpg")

    img = image.read(filename)

    shapes.line(img, (0, 0), (100, 100), shapes.RED, shapes.THICKNESS_THICK)
    shapes.rectangle(img, (100, 100), (350, 350), shapes.GREEN, shapes.THICKNESS_THICK)

    image.show("Shapes", img)


if __name__ == '__main__':
    start()
