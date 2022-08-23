import cv2
import os
import random
import math
import numpy as np
import time


IN_PATH = os.path.join("images", "dev_original", f"polyneuroparty.jpeg")
FPS = 1.4
SPF = 1 / 1.4
LENGTH = 50
OUT_PATH = os.path.join("images", "dev_processed", f"out_polyneuroparty.mp4")
IMG = cv2.imread(IN_PATH)
PURPLE_BASE = [66, 19, 85]
WHITE_BASE = [236, 245, 245]
OFF_WHITE_BASE = [216, 212, 223]

def main():
  imageToVideo(IMG, OUT_PATH, FPS, LENGTH)

def imageToVideo(img: cv2.Mat, out_path: str, fps: float, length: float):
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  output = cv2.VideoWriter(out_path, fourcc, fps, (img.shape[1], img.shape[0]), 1)
  write_length = 0
  last_was_original = False
  toAdd = __modImage(img)
  # cv2.imshow('orig', img)
  # cv2.imshow('mod', toAdd)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  # length = 2/fps + .2
  while write_length < length:
    print (write_length)
    if random.random() < .25 and not last_was_original:
      output.write(img)
      last_was_original = True
    else:
      toAdd = __modImage(img)
      output.write(toAdd)
      last_was_original = False
    write_length += (1 / fps)
    
  output.release()

def __modImage(img: cv2.Mat):
  img_copy = img.copy()
  alpha = .72
  overlay_this_color = np.array([random.randint(0, 256),random.randint(0, 256),random.randint(0, 256)])
  h = img.shape[0]
  w = img.shape[1]
  for y in range(h):
    for x in range(w):
      current_color = img[y][x]
      dif_between_colors = __getDiffBetweenColors(current_color, (0, 0, 0))
      if dif_between_colors < 90:
        continue
      # alpha = dif_between_colors / 480
      # alpha = (-.8/441) * dif_between_colors + .7
      newColor = cv2.addWeighted(img[y][x], alpha, overlay_this_color, 1 - alpha, 0, dtype=cv2.CV_8U)
      img_copy[y][x] = newColor.ravel()
  return img_copy
      


def __getDiffBetweenColors(p1, p2):
  b1, g1, r1 = p1
  b2, g2, r2 = p2
  return math.sqrt((b1 - b2)**2 + (g1 - g2)**2 + (r1 - r2)**2)

if __name__ == '__main__':
  main()