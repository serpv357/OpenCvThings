import cv2
import numpy as np
from bisect import bisect_left
import math

STUCKI_ERROR_DISTRIBUTION = ((2, 0), np.array([
  [0, 0, 0, 8, 4],
  [2, 4, 8, 4, 2],
  [1, 2, 4, 2, 1]
  ]))

def main():
  pass

def ditherColorSectorFloSte(img: cv2.Mat, width: int, height: int, pallete: list[tuple[int]]) -> cv2.Mat:
  if (img.ndim < 3):
    raise TypeError('Image not BGR')
  
  h = img.shape[0]
  w = img.shape[1]

  color_array_width = math.ceil(w / width)
  color_array_height = math.ceil(h / height)

  avg_color_error_array = np.zeros([color_array_height, color_array_width, 3], dtype=np.uint8)

  for y in range(color_array_height):
    for x in range(color_array_width):
      old_block = img[y*height:(y+1)*height][x*width:(x+1)*width]
      for row in old_block:
        for pix in row:
          pix += avg_color_error_array[y][x]

      old_block_average_color_row = np.average(old_block, axis=0)
      old_block_average_color = np.around(np.average(old_block_average_color_row, axis=0)).astype(np.uint8)
      new_block_average_color = __take_closest_color(old_block_average_color, pallete)
      cv2.rectangle(img, (x*width, y*height), ((x+1)*width, (y+1)*height), new_block_average_color, thickness=-1)
      error = old_block_average_color - new_block_average_color
      divd_error = error
      __applyErrorColorFloSte(avg_color_error_array, x, y, divd_error)
    
  return img
      


  

def __take_closest_color_rect(old_rect, pallette):
  avg_color = np.mean(old_rect)
  return __take_closest_color(avg_color, pallette)



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
  # __applyErrorColor(img, x + 1, y, divd_error * 8)
  # __applyErrorColor(img, x + 2, y, divd_error * 4)
  # __applyErrorColor(img, x - 2, y + 1, divd_error * 2)
  # __applyErrorColor(img, x - 1, y + 1, divd_error * 4)
  # __applyErrorColor(img, x, y + 1, divd_error * 8)
  # __applyErrorColor(img, x + 1, y + 1, divd_error * 4)
  # __applyErrorColor(img, x + 2, y + 1, divd_error * 2)
  # __applyErrorColor(img, x - 2, y + 2, divd_error)
  # __applyErrorColor(img, x - 1, y + 2, divd_error * 2)
  # __applyErrorColor(img, x, y + 2, divd_error * 4)
  # __applyErrorColor(img, x + 1, y + 2, divd_error * 2)
  # __applyErrorColor(img, x + 2, y + 2, divd_error)
  __applyErrorDistributionColor(img, x, y, divd_error, STUCKI_ERROR_DISTRIBUTION)

def __applyErrorDistributionColor(img, x, y, divd_error, error_distribution):
  error_center = error_distribution[0]
  nonrgb_dither_matrix = error_distribution[1]
  
  dither_matrix = np.full((nonrgb_dither_matrix.shape[0], nonrgb_dither_matrix.shape[1], 3), 0)
  for i in range(dither_matrix.shape[0]):
    for j in range(dither_matrix.shape[1]):
      for k in range(dither_matrix.shape[2]):
        dither_matrix[i][j][k] = nonrgb_dither_matrix[i][j]

  sx1 = x - error_center[0]
  sx2 = sx1 + dither_matrix.shape[1]
  x_left_error = max(0 - sx1, 0)
  x_right_error = max(sx2 - img.shape[1], 0)
  sy1 = y - error_center[1]
  sy2 = sy1 + dither_matrix.shape[0]
  y_top_error = max(0 - sy1, 0)
  y_bottom_error = max(sy2 - img.shape[0], 0)

  sx1 = sx1 + x_left_error
  sx2 = sx2 - x_right_error
  sy1 = sy1 + y_top_error
  sy2 = sy2 - y_bottom_error

  dsx1 = x_left_error
  dsx2 = dither_matrix.shape[1] - x_right_error
  dsy1 = y_top_error
  dsy2 = dither_matrix.shape[0] - y_bottom_error

  img[sy1:sy2,sx1:sx2] = np.clip(img[sy1:sy2,sx1:sx2].astype(np.int32) + dither_matrix[dsy1:dsy2,dsx1:dsx2] * divd_error, 0, 255).astype(np.uint8)



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