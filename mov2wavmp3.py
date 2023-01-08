import moviepy.editor as mp
import os


location = r'D:\ACTIVE\_MyOriginalRecordings\Edits\mp3\staging_area\temp\AmazingGrace_short.mp4'
output_folder = r'D:\ACTIVE\_MyOriginalRecordings\Edits\mp3'
filename = os.path.split(location)[1][:-4]

# use subclip to make clips subclip(seconds start, seconds end)
# clip = mp.VideoFileClip(location).subclip(7.5)
# clip = mp.VideoFileClip(location).subclip(342,350)
clip = mp.VideoFileClip(location)

# volume control - don't go over 2.5
clip = clip.volumex(2.2)


clip.audio.write_audiofile(os.path.join(output_folder,filename + ".mp3"))
clip.audio.write_audiofile(os.path.join(output_folder,filename + ".wav"))