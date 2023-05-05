from moviepy.editor import ImageClip,VideoFileClip,TextClip
# from PIL import Image 
# import cv2

def test_image_clip():
    fname = "data/10012.jpg"
    img = cv2.imread(fname)
    img = cv2.resize(img, (640, 480))
    # img = Image.open(fname)
    print(img.shape)
    print(type(img))

    clip = ImageClip(img,duration=1)
    clip.write_videofile("test.mp4",fps=24)


def test_video_clip():
    video_fname = "tmp.mp4"
    video_clip = VideoFileClip(video_fname)
    video_clip = video_clip.set_duration(3)
    print(video_clip.duration)
    # save 
    video_clip.write_videofile("tmp_3.mp4",fps=24)

def test_font():
    print( TextClip.list('font'))

if __name__ == "__main__":
    test_font()