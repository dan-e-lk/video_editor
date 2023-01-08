
# Do not use this.
# For some reason, the sound is not as good once converted to mp3 or wav or mp4 using pydub script.
# the sound is much better when edited through windows movie maker.

# in its simplest form:
# from pydub import AudioSegment
# AudioSegment.from_file("staging_area/KingOfHeaven.m4a").export("staging_area/example2.mp3", format="mp3")



# bulk convert all m4a, AND increase volume

import os
from pydub import AudioSegment

root_folder = r'D:\ACTIVE\_MyOriginalRecordings\Edits\mp3\staging_area\example'
song = AudioSegment.from_file(r"D:\ACTIVE\_MyOriginalRecordings\Edits\mp3\staging_area\YourGraceIsEnough.m4a", format='m4a')

# boost volume by 6dB
louder_song = song + 6

#save louder song 
louder_song.export("louder_song2_6db.mp3", format='mp3')


