import os
import cv2


myimage = cv2.imread("nusinh.png")
print(myimage.shape)
cv2.imshow('Hot Girl',myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize kích thước ảnh về 256 x 256 x 3

cv2.resize(myimage,(256,256), interpolation = cv2.INTER_AREA)
img_scaled = cv2.resize(myimage,(450, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaled Image', img_scaled)
print(img_scaled.shape)
cv2.imwrite('images\\hotgirl.png', img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Khởi tạo Pipeline cho quá trình sinh ảnh tăng cường
import Augmentor
path = "input"
p = Augmentor.Pipeline(path, output_directory="D:\\google-drive\\Computer Vision\\OpenCV\\Chương 10. Augment Reality\\output")

# applying a series of random transformations to image
p.rotate90(probability=0.5)

p.rotate270(probability=0.5)

p.flip_left_right(probability=0.75)

p.flip_top_bottom(probability=0.5)

p.crop_random(probability=1, percentage_area=0.5)

p.random_contrast(probability=0.5, min_factor=0, max_factor=1)	

p.resize(probability=1.0, width=256, height=256)

# bắt đầu thuật toán
p.sample(100)