import os, sys
import cv2
import numpy
from PIL import Image, ImageFont, ImageDraw
import dither

def main():
  path = ""
  down_path = ""
  img = cv2.imread(path)
  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ditherImage = dither.jjndDither(img)
  
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