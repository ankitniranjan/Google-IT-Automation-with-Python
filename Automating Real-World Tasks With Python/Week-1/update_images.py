# Put this file inside /images/ folder.


#!/usr/bin/env python3

import os, sys
from PIL import Image

size = (128,128)

for image in os.listdir():
	new_image = os.path.splitext(image)[0]
	
	try:
		with Image.open(image).covert('RGB') as im:
			im.thumbnail(size)
			im.rotate(270)
			im.save("/opt/icons/" + new_image, "JPEG")
			
	except:		# In case of (Hidden files(. and ..) and the file itself)
		pass
