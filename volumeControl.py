import moviepy.editor as mp
from moviepy.audio.fx.volumex import volumex
import os

input_folder = r'C:\Users\uniin\Music\_original\OriginalRecording\Good'
output_folder = r'C:\Users\uniin\Music\_original\Edits\Vol_control'

# create a list of movies found in the input folder
movies = [file for file in os.listdir(input_folder) if file.lower().endswith('.mov')]


for movie in movies:
	full_dir = os.path.join(input_folder,movie)
	new_filename = movie[:-4] + '.mp4'  # .mov to .mp4

	if new_filename not in os.listdir(output_folder):
		clip = mp.VideoFileClip(full_dir)
		newclip = clip.volumex(3) # 3 times the volume
		newclip.write_videofile(os.path.join(output_folder,new_filename))