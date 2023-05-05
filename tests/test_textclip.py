from moviepy.editor import TextClip, ImageClip,CompositeVideoClip
import math
from PIL import Image

import numpy 
def zoom_in_effect(clip, zoom_ratio=0.04):
    def effect(get_frame, t):
        img = Image.fromarray(get_frame(t))
        base_size = img.size

        new_size = [
            math.ceil(img.size[0] * (1 + (zoom_ratio * t))),
            math.ceil(img.size[1] * (1 + (zoom_ratio * t)))
        ]

        # The new dimensions must be even.
        new_size[0] = new_size[0] + (new_size[0] % 2)
        new_size[1] = new_size[1] + (new_size[1] % 2)

        img = img.resize(new_size, Image.LANCZOS)

        x = math.ceil((new_size[0] - base_size[0]) / 2)
        y = math.ceil((new_size[1] - base_size[1]) / 2)

        img = img.crop([
            x, y, new_size[0] - x, new_size[1] - y
        ]).resize(base_size, Image.LANCZOS)

        result = numpy.array(img)
        img.close()

        return result

    return clip.fl(effect)
one_text = "中文测试"
img  = "data/10012.jpg"
clip = ImageClip(img,duration=5)
clip = zoom_in_effect(clip, zoom_ratio=0.04)

text_clip = TextClip(one_text, font='幼圆',fontsize=70, color='red')
text_clip = text_clip.set_duration(5)

clip = CompositeVideoClip([clip,text_clip.set_position(('center','bottom'))])
clip.write_videofile("text_test.mp4", fps=24)

# print(TextClip.list('font'))