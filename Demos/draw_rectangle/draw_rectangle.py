#!/usr/bin/env python
import os
import Image
import ImageDraw

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)

BLACK = "#000000"
WHITE = "#ffffff"

canvas_w, canvas_h = 100, 100
im = Image.new(mode="RGB", size=(canvas_w, canvas_h), color=WHITE)

draw = ImageDraw.Draw(im=im)

left_top_x, left_top_y = 10, 10
right_bottom_x, right_bottom_y = 30, 100
box = (left_top_x, left_top_y, right_bottom_x, right_bottom_y)

draw.rectangle(xy=box, fill=BLACK, outline=None)

im.save(os.path.join(PWD, "draw_rectangle.jpg"))
