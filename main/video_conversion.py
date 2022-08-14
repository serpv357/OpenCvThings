import cv2

def convertToGrayscale(original_path: str, out_path: str):
  vid_capture = cv2.VideoCapture(original_path)
  frame_width = int(vid_capture.get(3))
  frame_height = int(vid_capture.get(4))
  frame_size = (frame_width,frame_height)
  fps = vid_capture.get(5)
  length = int(vid_capture.get(cv2.CAP_PROP_FRAME_COUNT))
  frame_no = 1
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  output = cv2.VideoWriter(out_path, fourcc, fps, frame_size, 0)
  print('total frames',length)
  while (vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
      print('current frame', frame_no)
      frame_no += 1
      grayscaleFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      output.write(grayscaleFrame)
    else:
      print('Stream disconnected')
      break
  vid_capture.release()
  output.release()
