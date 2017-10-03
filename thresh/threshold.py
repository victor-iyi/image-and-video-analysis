"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 20 September, 2017 @ 3:52 PM.
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2


def binary(img, thresh_val, maxval, thresh_type=cv2.THRESH_BINARY, grayscale=True,
           display=False):
    """
    Binary threshold.

    The function applies fixed-level thresholding to a multiple-channel array.
    The function is typically used to get a bi-level (binary) image out of a grayscale
    image ( cv::compare could be also used for this purpose) or for removing a noise,
    that is, filtering out pixels with too small or too large values. There are several
    types of thresholding supported by the function. They are determined by type parameter.

    Also, the special values cv::THRESH_OTSU or cv::THRESH_TRIANGLE may be combined with one of the
    above values. In these cases, the function determines the optimal threshold value using the Otsu's
    or Triangle algorithm and uses it instead of the specified thresh . The function returns the
    computed threshold value. Currently, the Otsu's and Triangle methods are implemented only for 8-bit
    images.

    @note Input image should be single channel only in case of CV_THRESH_OTSU or CV_THRESH_TRIANGLE flags
    :param img:
            input array (multiple-channel, 8-bit or 32-bit floating point).
    :param thresh_val:
            threshold value.
    :param maxval:
            maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV
            thresholding types.
    :param thresh_type:
            thresholding type (see the cv::ThresholdTypes).
    :param grayscale:
            Converts the image to grayscale before applying threshold
    :param display:
            If set to true the thresheld image is displayed
    :return:
            A threshold image.
    """
    if grayscale:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img, thresh_val, maxval, thresh_type)
    if display:
        cv2.imshow('Binary Threshold', img_thresh)
    return img_thresh


def adaptive(img, maxval, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
             thresh_type=cv2.THRESH_BINARY, block_size=13,
             C=19, display=False):
    """
    Adaptive threshold.

    The function transforms a grayscale image to a binary image according to the formulae:
        The function can process the image in-place.

    :param img:
            Source 8-bit single-channel image.
    :param maxval:
            Non-zero value assigned to the pixels for which the condition is satisfied
    :param method:
            Adaptive thresholding algorithm to use, see cv::AdaptiveThresholdTypes
    :param thresh_type:
            Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV,
            see cv::ThresholdTypes.
    :param block_size:
            Size of a pixel neighborhood that is used to calculate a threshold value for the
            pixel: 3, 5, 7, and so on.
    :param C:
            Constant subtracted from the mean or weighted mean (see the details below). Normally, it
            is positive but may be zero or negative as well.
    :param display:
            If set to true the thresheld image is displayed

    :return:
            A threshold image.
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.adaptiveThreshold(img, maxval, method,
                                       thresh_type, block_size, C)
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
