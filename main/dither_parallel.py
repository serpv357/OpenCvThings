import cv2
import numpy
import math
import multiprocessing

# all this crap doesnt work but will put future parallelized dithering implementations in here


def ditherColorFlosteBlockParallel(img: cv2.Mat, pallete: list[tuple[int]]):
  _ditherWholeImage(img, pallete)

def _PrimalBlock(M: int, N: int, a: int, b: int, itr: int):
  if itr > 0 and itr <= N/b:
    row = 1
    col = itr
  else:
    row = int(math.ceil((itr - (N/b))/2))
    col = int((N/b) - ((itr - N/b) % 2))
  return (row, col)

def _ditherWholeImage(I: cv2.Mat, pallete: list[tuple[int]]):
  M = I.shape[0]
  N = I.shape[1]
  a = M / 6
  b = N / 6

  iters = 2 * (M/a) + (N/b)

  for i in range(1, int(iters)):
    pb = _PrimalBlock(M, N, a, b, i)
    print(f"iter: {i} row: {pb[0]} col: {pb[1]}")



