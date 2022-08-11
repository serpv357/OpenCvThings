import cv2
import numpy as np
from bisect import bisect_left
import math

overflow_counter = 0

def main():
  pass

def jjndDitherColorFloste(old_image: cv2.Mat) -> cv2.Mat:
  h = old_image.shape[0]
  w = old_image.shape[1]
  new_image = old_image.copy()
  for y in range(h):
    for x in range(w):
      old = old_image[y][x]
      new = take_closest_color([(128, 0, 128), (0, 128, 128), (255, 255, 224)], old)
      new_image[y][x][0] = new[0]
      new_image[y][x][1] = new[1]
      new_image[y][x][2] = new[2]
      error = old - new
      apply_error_color(old_image, x+1, y, error * 7/16)
      apply_error_color(old_image, x-1, y+1, error * 3/16)
      apply_error_color(old_image, x, y+1, error * 5/16)
      apply_error_color(old_image, x+1, y+1, error * 1/16)
    
  return new_image

def jjndDitherFloste(old_image: cv2.Mat) -> cv2.Mat:
  old_image = cv2.cvtColor(old_image, cv2.COLOR_BGR2GRAY)
  h = old_image.shape[0]
  w = old_image.shape[1]
  new_image = np.zeros((h, w), dtype=np.uint8)
  for y in range(h):
    for x in range(w):
      old = old_image[y][x]
      new = take_closest([0, 255], old)
      new_image[y][x] = new
      error = old - new
      apply_error(old_image, x+1, y, error * 7/16)
      apply_error(old_image, x-1, y+1, error * 3/16)
      apply_error(old_image, x, y+1, error * 5/16)
      apply_error(old_image, x+1, y+1, error * 1/16)
    
  return new_image

def apply_error_color(arr, x, y, error):
  b, g, r = error
  for i, c in enumerate([b, g, r]):
    if (0 < y < len(arr)):
      if (0 < x < len(arr[0])):
        end = arr[y][x][i] + c
        if end > 255 or end < 0:
          return
        arr[y][x][i] += error[i]

def apply_error(arr, x, y, error):
  if (0 < y < len(arr)):
    if (0 < x < len(arr[0])):
      end = arr[y][x] + error
      if end > 255 or end < 0:
        return
      arr[y][x] += error

def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

def take_closest_color(myList, p):
  b, g, r = p
  index_of_closest = 0
  maxdiff = 9999999999
  for i, color in enumerate(myList):
    cb = color[0]
    cg = color[1]
    cr = color[2]
    if math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2) < maxdiff:
      maxdiff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
      index_of_closest = i
  return myList[index_of_closest]



if __name__ == '__main__':
  main()