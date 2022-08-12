import cv2
import dither
import os

def main():
  imgName = "rain_temple.jpeg"
  path = os.path.join("images", "original", imgName)
  stucki_path = os.path.join("images", "processed", f"stucki_{imgName}")
  #rect_path = os.path.join("images", "processed", f"stucki_{imgName}")

  img = cv2.imread(path)

  stuckiDitherImage = dither.ditherColorStucki(img, [(121, 20, 116), (49, 120, 124), (213, 255, 241)])

  #rectDitherImage = dither.ditherColorSectorFloSte(img2, 3, 3, [(128, 0, 128), (55, 29, 50), (255, 255, 224)])

  # cv2.imshow('rectangular_dither', rectDitherImage)
  # cv2.imwrite(rect_path, rectDitherImage)
  
  cv2.imshow('stucki', stuckiDitherImage)
  cv2.imwrite(stucki_path, stuckiDitherImage)


  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()