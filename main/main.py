import cv2
import dither
import os

def main():
  imgName = "dali.jpeg"
  path = os.path.join("images", "original", imgName)
  floste_path = os.path.join("images", "processed", f"floste_{imgName}")
  stucki_path = os.path.join("images", "processed", f"stucki_{imgName}")
  stucki_pallete_converted_path = os.path.join("images", "processed", f"stucki_pconverted_{imgName}")
  img = cv2.imread(path)
  img2 = img.copy()
  img3 = img.copy()
  # flosteDitherImage = dither.ditherColorFloSte(img, [(18, 18, 216), (216, 104, 18), (255, 255, 224)])
  stuckiDitherImage = dither.ditherColorStucki(img2, [(167, 51, 254), (29, 201, 171), (237, 206, 176)])
  # stuckiPConvertedDitherImage = dither.ditherColorStucki(
  #   img3, 
  #   [(146, 220, 238), (72, 70, 43), (135, 159, 160)], 
  #   {
  #     (146, 220, 238): (255, 201, 21)
  #   }
  #   )
  # stucki_pallete_converted_path
  
  #cv2.imshow('floste', flosteDitherImage)
  cv2.imshow('stucki', stuckiDitherImage)
  #cv2.imshow('stucki_pconverted', stuckiPConvertedDitherImage)
  #cv2.imwrite(floste_path, flosteDitherImage)
  cv2.imwrite(stucki_path, stuckiDitherImage)
  #cv2.imwrite(stucki_pallete_converted_path, stuckiPConvertedDitherImage)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()