import cv2
import dither
import os
import dither_parallel
import io
import imageio
import video_conversion

def main():
  #ditherImageExample()


  imgName = "ed_new.png"
  path = os.path.join("images", "dev_original", imgName)
  stucki_path = os.path.join("images", "dev_processed", f"stucki_{imgName}")
  # #rect_path = os.path.join("images", "processed", f"stucki_{imgName}")
  #gif_path = os.path.join("images", "dev_processed", f"video_2_{imgName}")
  # vid_path = os.path.join("images", "dev_processed", f"video_gray_{imgName}")
  img = cv2.imread(path)

  # pallete = [(0, 0, 252), (255, 255, 255), (94, 240, 112), (174, 203, 247), (64, 188, 237), (0, 0, 0) ]
  pallete = [(0, 0, 0), (255, 255, 255)]
  #conversion_pallete = {(51, 72, 133): (25, 38, 227)}

  # dither_parallel.ditherColorFlosteBlockParallel(img, [(199, 85, 155), (140, 255, 253), (251, 253, 252), (242, 215, 41)])

  #vid = cv2.VideoCapture(path)

  # video_conversion.convertToGrayscale(path, vid_path)

  #dither.ditherVideo(vid, pallete, vid_path)

  #gif_frames = dither.ditherGif(path, pallete)

  #imageio.mimsave(gif_path, gif_frames, fps=20)
  #img = cv2.imread(path)

  
  stuckiDitherImage = dither.ditherColorStucki(img, pallete)

  # rectDitherImage = dither.ditherColorSectorFloSte(img2, 3, 3, [(128, 0, 128), (55, 29, 50), (255, 255, 224)])

  # cv2.imshow('rectangular_dither', rectDitherImage)
  # cv2.imwrite(rect_path, rectDitherImage)
  
  cv2.imshow('stucki', stuckiDitherImage)
  cv2.imwrite(stucki_path, stuckiDitherImage)


  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
  