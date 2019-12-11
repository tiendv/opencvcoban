import sys
import os
import cv2
import Augmentor

path_folder = "\\home\\mmlab\\workspace\\projects-CV\\Augmented-Data\\img70k"
os.mkdir("\\home\\mmlab\\workspace\\projects-CV\\Augmented-Data\\augmented-data")

for folder in os.listdir(path_folder):
	os.mkdir("\\home\\mmlab\\workspace\\projects-CV\\Augmented-Data\\augmented-data\\" + str(folder))	
	for path_image in listdir(folder):
		if not (path_image.endswith('.jpg') or path_image.endswith('.png')):
			continue
		os.mkdir("\\home\\mmlab\\workspace\\projects-CV\\Augmented-Data\\augmented-data\\" + str(folder) + str(path_image))
		output = "\\home\\mmlab\\workspace\\projects-CV\\Augmented-Data\\augmented-data\\" + str(folder) + str(path_image)
		p = Augmentor.Pipeline(source_directory=path_image, output_directory=output, )