#!/usr/bin/env python
"""
copy image
"""
import os
PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)

import Image

file_path = os.path.join(parent_path, "image_resources", "l_hires.jpg")
im = Image.open(fp = file_path)

left_upper_x, left_upper_y = 10, 10
right_lower_x, right_lower_y = 50, 50
box = (left_upper_x, left_upper_y, right_lower_x, right_lower_y)

region = im.crop(box)

region = region.transpose(Image.ROTATE_90)
im.paste(region, box)

new_filename = "C-c-C-v-left" + ".jpg"
im.save(new_filename)