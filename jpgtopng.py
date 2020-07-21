import sys
import os
from PIL import Image

img_folder = sys.argv[1]
op_folder = sys.argv[2]

if not os.path.exists(op_folder):
	os.makedirs(op_folder)

for filename in os.listdir(img_folder):
	img = Image.open(f'{img_folder}{filename}')
	name = os.path.splitext(filename)[0]
	img.save(f'{op_folder}{name}.png','png')
	print('done')
