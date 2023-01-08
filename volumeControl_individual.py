# warning: increasing volume could crack the sound

import moviepy.editor as mp
from moviepy.audio.fx.volumex import volumex
import os

input_file = r'D:\ACTIVE\_MyOriginalRecordings\Edits\Deliverable\220313_예수사랑해요_왕이신_주품에_형제의.mp4'
output_folder = r'D:\ACTIVE\_MyOriginalRecordings\Edits\Vol_control'

new_filename = os.path.split(input_file)[1][:-4] + '_Vx2.mp4'  

if new_filename not in os.listdir(output_folder):
	clip = mp.VideoFileClip(input_file)
	newclip = clip.volumex(2) # 2 times the volume
	newclip.write_videofile(os.path.join(output_folder,new_filename))