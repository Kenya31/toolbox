# -*- coding:utf-8 -*-
import sys

import cv2
from pyzbar.pyzbar import decode

ARGV = sys.argv


# Print usage.
def print_usage():
    print("")
    print("Usage: python {0} <QR code image file>".format(argv[0]))
    print("")


# Main routine.
def main(img_file):
    print("DEBUG imgFile[{0}]".format(img_file))

    # Load image
    img = cv2.imread(img_file)
    data = decode(img)

    return data[0][0].decode("utf-8", "ignore")


if __name__ == "__main__":

    if 2 != len(ARGV):
        print_usage()
    else:
        RESULT = main(ARGV[1])
        print("QR code RESULT[{0}]".format(RESULT))
