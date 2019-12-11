import sys
import os
import cv2
import Augmentor

def augment(path, number, output):
	"""
	# Parameters: 
	#	- image is the reference to the image we want to augment data
	#	- number is the number of augmented images
	# Return Value: a list of augmented images.
	"""

	# Init Pipeline
	p = Augmentor.Pipeline(path, output_directory=output)

	# applying a series of random transformations to image
	p.rotate90(probability=0.5)

	p.rotate270(probability=0.5)

	p.flip_left_right(probability=0.75)

	p.random_

	p.flip_top_bottom(probability=0.5)

	p.random_color(probability = 0.5, min_factor=0, max_factor=1)

	p.random_contrast(probability=0.5, min_factor=0, max_factor=1)

	p.crop_random(probability=0.5)
	
	p.resize(probability=1.0, width=128, height=128)

	# bắt đầu thuật toán
	p.sample(number)


def augment_data(path, number):
	"""
	# Parameter:
	# - number is the number of augmented images for each image.
	# This is main function for augment dataset. 
	"""
	for folder in os.listdir(path):
		print(big_folder)
		os.mkdir("/home/mmlab/workspace/projects-CV/Augmentation-data/augmented-data/" + str(folder))
		for image in os.listdir(big_folder):
			# Make the folder contain augmented data
			os.mkdir("\\home\\mmlab\\workspace\\projects-CV\\Augmentation-data\\augmented-data\\" + str(folder) + '\\' + str(image))
			output = "\\home\\mmlab\\workspace\\projects-CV\\Augmentation-data\\augmented-data\\" + str(folder) + '\\' + str(image)
			if image.endswith(".png") or image.endswith(".jpg"):
				print(image)
				augment(image, number, output)


if __name__ == '__main__':
	path = "\\home\\mmlab\\workspace\\projects-CV\\Augmentation-data\\img70k"
	augment_data(path, 10)