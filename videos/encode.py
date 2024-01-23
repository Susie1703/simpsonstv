import os
from pathlib import Path
import fnmatch

newFiles = []
oldFiles = []
directory = os.path.dirname(os.path.realpath(__file__))
#directory = list(Path(".").rglob("*.*"))
destinationDirectory = "E:\Downloads\encoded"

for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, '*.*'):
        oldFiles.append(os.path.join(root, filename))

print('list of files %s' % directory)

if not os.path.exists(destinationDirectory):
	os.mkdir(destinationDirectory)


def isVideo(videofile):
	if videofile.lower().endswith('.mp4'):
		return True
	if videofile.lower().endswith('.mkv'):
		return True
	if videofile.lower().endswith('.mov'):
		return True
	if videofile.lower().endswith('.avi'):
		return True
	return False

newFiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for filename in fnmatch.filter(filenames, '*.*') for f in filenames if isVideo(f)]

for filepath in newFiles:
	video = os.path.basename(filepath)
	videoName = os.path.splitext(video)[0]
	newFile = '%s.mp4' % videoName
	i = filepath
	o = os.path.join(destinationDirectory, newFile)
	if os.path.isfile(o):
		continue
	encodeCommand = 'ffmpeg -i "%s" -vf scale=-2:480 -c:v libx264 -profile:v baseline -level 3.0 -preset fast -crf 23 -pix_fmt yuv420p "%s"' % (i, o)
	print('Encoding %s' % newFile)
	encode = os.popen(encodeCommand).read()
