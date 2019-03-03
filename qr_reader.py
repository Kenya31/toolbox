# -*- coding:utf-8 -*-
import cv2
from pyzbar.pyzbar import decode
import sys


def main(imgFile):
    print("DEBUG fileName[{0}]".format(imgFile))

    # Load image
    img = cv2.imread(imgFile)
    data = decode(img)

    return data[0][0].decode("utf-8", "ignore")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 2:
        data = main(argv[1])
        print("{0}".format(data))
    else:
        print("{0}".format(argv[0]))
