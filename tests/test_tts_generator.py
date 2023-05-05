import sys
import os
# sys.path.append("F:\Workspace\github\open-chat-video-editor")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generator.tts.build import TTSGenerator 
from configs.config import get_cfg_defaults  # local variable usage pattern, or:
from generator.tts.build import build_tts_generator

def test_PaddleSpeechTTS():
    cfg = get_cfg_defaults()
    cfg_path = "configs\multilang_image_by_retrieval.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    tts_generator = build_tts_generator(cfg)
    text = ["a cat on the road",'a cat and a kid playing on the road']
    resp = tts_generator.batch_run(text)
    print(resp)
if __name__ == "__main__":
    test_PaddleSpeechTTS()
    