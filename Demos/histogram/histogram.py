#!/usr/bin/env python
import os
PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)

import Image, ImageDraw

file_path = os.path.join(parent_path, "image_resources", "captcha.jpg")

BLACK = 0
WHITE = 255
# white(255) ~ black(0)

im = Image.open(fp = file_path)
w, h = im.size[0], im.size[1]

print "width:", w
print "high:", h


im = im.draft("L", im.size)

pixsels = im.load()


for x in xrange(w):
    for y in xrange(h):
        if pixsels[x, y] > 128:
            pixsels[x, y] = WHITE
        else:
            pixsels[x, y] = BLACK


counts = []
for x in xrange(w):
    count = len([1 for y in xrange(h)
                if pixsels[x, y] is BLACK])

    counts.append(count)


hist_im = Image.new(mode="L", size=(w, h), color=WHITE)
draw = ImageDraw.Draw(hist_im)
h_step = h / max(counts)

for x in xrange(w):
    left_top_x, left_top_y = x, h - counts[x] * h_step
    right_bottom_x, right_bottom_y = x + 1, h
    box = (left_top_x, left_top_y, right_bottom_x, right_bottom_y)
    draw.rectangle(xy=box, fill=BLACK)

new_file_name = os.path.splitext(os.path.basename(file_path))[0]
new_file_name = new_file_name + '-' + 'histogram' + '.bmp'

hist_im.save(new_file_name)
