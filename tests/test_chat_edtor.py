import sys
import os
# sys.path.append("F:\Workspace\github\open-chat-video-editor")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from editor.build import build_editor
from configs.config import get_cfg_defaults  # local variable usage pattern, or:

def test_editor():
    cfg = get_cfg_defaults()
    cfg_path = "configs\multilang_image_by_retrieval.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('toy test')

def test_image_by_retrieval_text_by_zhtoytextgen():
    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_retrieval_text_by_zhtoytextgen.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('toy test',"","image_by_retrieval_text_by_zhtoytextgen.mp4")

def test_editor_by_video_retrieval():
    cfg = get_cfg_defaults()
    cfg_path = "configs/video_by_retrieval.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('toy test')
# video_by_retrieval_text_by_zhtoytextgen


def test_editor_by_video_by_retrieval_text_by_zhtoytextgen():
    cfg = get_cfg_defaults()
    cfg_path = "configs/video_by_retrieval_text_by_zhtoytextgen.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('小孩子养宠物',"","video_by_retrieval_text_by_zhtoytextgen.mp4")
    
    
def test_editor_by_video_retrieval_chatgpt_zh():
    cfg = get_cfg_defaults()
    cfg_path = "configs/video_by_retrieval_text_by_chatgpt_zh.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('小孩子养宠物',"","video_retrieval_chatgpt_zh.mp4")

def test_editor_by_image_diffusion():
    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_diffusion.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('toy test',"",'test_en_image_diffusion.mp4')

def test_editor_zh_by_image_diffusion():
    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_diffusion_text_by_zhtoytextgen.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('toy test',"",'test_zh_image_diffusion.mp4')

def test_editor_chatgpt_zh_by_image_diffusion():
    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_diffusion_text_by_chatgpt_zh.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    editor.run('小孩子养宠物',"picture of no words",'test_chatgpt_zh_image_diffusion.mp4')


def test_editor_by_image_retrieval_then_diffusion():

    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_retrieval_then_diffusion_zhtoytextgen.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('toy test',"",'image_by_retrieval_then_diffusion_zhtoytextgen.mp4')
    

def test_editor_by_image_retrieval_then_diffusion_chatgpt_zh():

    cfg = get_cfg_defaults()
    cfg_path = "configs/image_by_retrieval_then_diffusion_chatgpt_zh.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('小孩子养宠物',"",'image_by_retrieval_then_diffusion_chatgpt_zh.mp4')

def test_image_by_diffusion_text_by_ZhToyURL2TextModel():
    cfg = get_cfg_defaults()
    cfg_path = "configs/url2video/image_by_diffusion_text_by_ZhToyURL2TextModel.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('',"",'image_by_diffusion_text_by_ZhToyURL2TextModel.mp4')

def test_image_by_retrieval_text_by_ZhToyURL2TextModel():
    cfg = get_cfg_defaults()
    cfg_path = "configs/url2video/image_by_retrieval_text_by_ZhToyURL2TextModel.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('',"",'image_by_retrieval_text_by_ZhToyURL2TextModel.mp4')

# image_by_retrieval_then_diffusion_ZhToyURL2TextModel

def test_image_by_retrieval_then_diffusion_ZhToyURL2TextModel():
    cfg = get_cfg_defaults()
    cfg_path = "configs/url2video/image_by_retrieval_then_diffusion_ZhToyURL2TextModel.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('',"",'image_by_retrieval_then_diffusion_ZhToyURL2TextModel.mp4')

def test_video_by_retrieval_text_by_ZhToyURL2TextModel():
    cfg = get_cfg_defaults()
    cfg_path = "configs/url2video/video_by_retrieval_text_by_ZhToyURL2TextModel.yaml"
    cfg.merge_from_file(cfg_path)
    print(cfg)
    editor = build_editor(cfg)
    style = "cartoon style"
    editor.run('',"",'video_by_retrieval_text_by_ZhToyURL2TextModel.mp4')

if __name__ == "__main__":
    test_video_by_retrieval_text_by_ZhToyURL2TextModel()
    