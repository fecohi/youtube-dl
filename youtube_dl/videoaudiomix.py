# using moviepy to mix audio and video geting the file names as parameters and composing the final file name with the original video file name
# the final file is saved in the same folder as the original video file

from moviepy.editor import *
import sys

video = sys.argv[1]
audio = sys.argv[2]
final = video[:-4] + "_final.mp4"

videoclip = VideoFileClip(video)
audioclip = AudioFileClip(audio)

videoclip = videoclip.set_audio(audioclip)
videoclip.write_videofile(final)