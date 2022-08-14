import av
import os
import ffmpeg

with_audio_path = os.path.join('images', 'dev_original',"")
without_audio_path = os.path.join("images", "dev_processed", '')
merged_out_path = os.path.join('images', 'dev_processed', '')

def main():
  applyAudioFromVideoToAudiolessVidioFfmpeg(with_audio_path, without_audio_path, merged_out_path)

def applyAudioFromVideoToAudiolessVidioFfmpeg(with_audio_path: str, without_audio_path: str, merged_out_path: str):
  '''
  Need to be the same original videos or wont have same stuff at same frames.
  '''
  video = ffmpeg.input(without_audio_path)
  audio = ffmpeg.input(with_audio_path)
  ffmpeg.concat(video, audio, v=1, a=1).output(merged_out_path).run()

if __name__ == '__main__':
  main()
