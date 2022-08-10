import os, sys
import cv2
import numpy
from PIL import Image, ImageFont, ImageDraw
import dither

def main():
  path = "/Users/sergei/Downloads/qt_2.jpeg"
  down_path = "/Users/sergei/Documents/Repos/OpenCVThings/OpenCvThings/images/qtqtqt.jpeg"
  img = cv2.imread(path)
  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #ditherImage = dither.ditherColorStucki(img, [(29, 233, 233), (94, 255, 0), (202, 20, 117)])
  ditherImage = dither.ditherColorFloSte(img, [(128, 0, 128), (0, 128, 128), (255, 255, 224)])
  
  # cv2.imshow('Original image', img)
  # cv2.imshow('Gray image', grayImg)
  cv2.imshow('ditha', ditherImage)
  cv2.imwrite(down_path, ditherImage)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

  
def imgToAscii(cv2Img):
  grayImg = cv2.cvtColor(cv2Img, cv2.COLOR_BGR2GRAY)



if __name__ == '__main__':
  main()