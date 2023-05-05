import sys
import os
# sys.path.append("F:\Workspace\github\open-chat-video-editor")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PIL import Image
from generator.image.build import build_image_generator
from configs.config import get_cfg_defaults  # local variable usage pattern, or:

def test_image_by_retrieval():
    cfg = get_cfg_defaults()
    cfg_path = "configs\image_by_retrieval.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    # build image generator
    image_generator = build_image_generator(cfg)
    text = ["a cat",'a cat and a kid']
    image_resp = image_generator.batch_run(text)
    print(image_resp)
    for item in image_resp:
        img = Image.open(item['img_local_path'])

def test_multilang_image_by_retrieval():
    cfg = get_cfg_defaults()
    cfg_path = "configs\multilang_image_by_retrieval.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    # build image generator
    image_generator = build_image_generator(cfg)
    text = ["一只猫",'一只猫和一个孩子']
    image_resp = image_generator.batch_run(text)
    print(image_resp)
    for item in image_resp:
        img = Image.open(item['img_local_path'])
 
if __name__ == "__main__":
    test_image_by_retrieval()