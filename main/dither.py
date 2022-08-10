import cv2
import numpy as np
from bisect import bisect_left
import math

def main():
  pass

def ditherColorStucki(img: cv2.Mat, pallete: list[tuple[int]], pallete_conversion_map : dict[tuple[int], tuple[int]] = None) -> cv2.Mat:
  '''
  Assumes input is BGR image, and returns a BGR image dithered with Stucki dithering.

  Takes a pallete parameter which is a list of 3-length tuples representing BGR values which are the possible colors for the final image.
  
  If the optional pallete_conversion_map param is passed in it is used to convert pixels which match its keys into its values for the final image, post-dithering.
  So if a pixel close to pure red would be set as red in normal dithering, and you mapped red to teal in pallete_conversion_map, it would instead be teal in the final image.
  '''
  if (img.ndim < 3):
    raise TypeError('Image not BGR')

  h = img.shape[0]
  w = img.shape[1]
  for y in range(h):
    for x in range(w):
      old_p = img[y][x]
      new_p = __take_closest_color(old_p, pallete)
      error = old_p - new_p
      divd_error = error / 42


      if pallete_conversion_map != None:
        if new_p in pallete_conversion_map:
          new_p = pallete_conversion_map[new_p]
      img[y][x] = new_p

      __applyErrorColorStucki(img, x, y, divd_error)
  
  return img

def ditherColorFloSte(img: cv2.Mat, pallete: list[tuple[int]], pallete_conversion_map : dict[tuple[int], tuple[int]] = None) -> cv2.Mat:
  '''
  Assumes input is BGR image, and returns a BGR image dithered with Floyd-Steinberg Dithering.

  Takes a pallete parameter which is a list of 3-length tuples representing BGR values which are the possible colors for the final image.
  
  If the optional pallete_conversion_map param is passed in it is used to convert pixels which match its keys into its values for the final image, post-dithering.
  So if a pixel close to pure red would be set as red in normal dithering, and you mapped red to teal in pallete_conversion_map, it would instead be teal in the final image.
  '''
  if (img.ndim < 3):
    raise TypeError('Image not BGR')

  h = img.shape[0]
  w = img.shape[1]
  for y in range(h):
    for x in range(w):
      old_p = img[y][x]
      new_p = __take_closest_color(old_p, pallete)
      error = old_p - new_p
      divd_error = error / 16


      if pallete_conversion_map != None:
        if new_p in pallete_conversion_map:
          new_p = pallete_conversion_map[new_p]
      img[y][x] = new_p

      __applyErrorColorFloSte(img, x, y, divd_error)
  
  return img

def __applyErrorColorFloSte(img, x, y, divd_error):
  __applyErrorColor(img, x + 1, y, 7 * divd_error)
  __applyErrorColor(img, x - 1, y + 1, 3 * divd_error)
  __applyErrorColor(img, x, y + 1, 5 * divd_error)
  __applyErrorColor(img, x + 1, y + 1,  divd_error)


def __applyErrorColorStucki(img, x, y, divd_error):
  __applyErrorColor(img, x + 1, y, divd_error * 3)
  __applyErrorColor(img, x + 2, y, divd_error * 1)
  __applyErrorColor(img, x - 2, y + 1, divd_error * 1)
  __applyErrorColor(img, x - 1, y + 1, divd_error * 2)
  __applyErrorColor(img, x, y + 1, divd_error * 3)
  __applyErrorColor(img, x + 1, y + 1, divd_error * 2)
  __applyErrorColor(img, x + 2, y + 1, divd_error * 1)
  __applyErrorColor(img, x - 2, y + 2, divd_error * 0)
  __applyErrorColor(img, x - 1, y + 2, divd_error * 1)
  __applyErrorColor(img, x, y + 2, divd_error * 2)
  __applyErrorColor(img, x + 1, y + 2, divd_error * 1)
  __applyErrorColor(img, x + 2, y + 2, divd_error)

def __applyErrorColor(img, x, y, error):
  b, g, r = error
  for i, c in enumerate([b, g, r]):
    if (0 < y < len(img)):
      if (0 < x < len(img[0])):
        end = img[y][x][i] + c
        if end > 255:
          img[y][x][i] = 255
          return
        if end < 0:
          img[y][x][i] = 0
          return
        img[y][x][i] = round(img[y][x][i] + c)


def __take_closest_color(p, pallete: list[tuple[int]]) -> tuple[int]:
  max_diff = __getDiffBetweenPixels(p, pallete[0])
  closest = pallete[0]
  for c in pallete[1:]:
    if __getDiffBetweenPixels(p, c) < max_diff:
      closest = c
  return closest

def __getDiffBetweenPixels(p1, p2):
  b1, g1, r1 = p1
  b2, g2, r2 = p2
  return math.sqrt((b1 - b2)**2 + (g1 - g2)**2 + (r1 - r2)**2)


def ditherGrayStucki(imag: cv2.Mat, ) -> cv2.Mat:
  '''
  Assumes input is BGR or Grayscale image, and returns a Grayscale image dithered with Stucki dithering.
  '''
  pass


if __name__ == '__main__':
  main()