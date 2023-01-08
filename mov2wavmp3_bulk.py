import moviepy.editor as mp
import os



def conv_all_to_mp3(parent_path, output_folder, vid_format = '.mp4', aud_format = ['.mp3','.wav']):

	for root, dirs, files in os.walk(parent_path, topdown=False):
		for name in files:
			file_fullpath = os.path.join(root, name)

			if file_fullpath.endswith(vid_format):
				location = file_fullpath
				filename = os.path.split(location)[1][:-4]

				# use subclip to make clips subclip(seconds start, seconds end)
				# clip = mp.VideoFileClip(location).subclip(7.5)
				# clip = mp.VideoFileClip(location).subclip(342,350)
				clip = mp.VideoFileClip(location)

				# volume control #2.5 is usually the max you go
				clip = clip.volumex(2)

				for i in aud_format:
					clip.audio.write_audiofile(os.path.join(output_folder,filename + i))



if __name__ == '__main__':
	# parent path (all .mp4 files in this folder (and its subfolders) will be converted to mp3)
	parent_path = r'D:\ACTIVE\_MyOriginalRecordings\Edits\mp3\staging_area\temp'
	output_folder = r'D:\ACTIVE\_MyOriginalRecordings\Edits\mp3\best'
	conv_all_to_mp3(parent_path, output_folder)