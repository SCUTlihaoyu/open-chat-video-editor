import gradio as gr
import argparse
import sys
import os
# sys.path.append("F:\Workspace\github\open-chat-video-editor")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from editor.build import build_editor
from configs.config import get_cfg_defaults  # local variable usage pattern, or:
from comm.mylog import logger

def get_args():

    parser = argparse.ArgumentParser(description='config for open chat editor')
    parser.add_argument('--cfg', type=str, required=True,help='input cfg file path')
    parser.add_argument('--func', type=str,default='Text2VideoEditor',help='editor function name')
    args = parser.parse_args()
    return args
if __name__ == "__main__":
    args = get_args()
    cfg_path = args.cfg
    if args.func == "Text2VideoEditor":
        logger.info('building Text2VideoEditor')
        cfg = get_cfg_defaults()
        # cfg_path = "configs/video_by_retrieval_text_by_chatgpt_zh.yaml"
        cfg.merge_from_file(cfg_path)
        print(cfg)
        editor = build_editor(cfg)
        def run_Text2VideoEditor_logit(input_text, style_text):
            out_video = "test.mp4"
            out_text,video_out = editor.run(input_text,style_text,out_video)
            return out_text,video_out
        def run_Text2VideoEditor_ui():
            gr.Interface(
                run_Text2VideoEditor_logit,
                [gr.inputs.Textbox(placeholder="Enter sentence here..."),  gr.Radio(["realism style", "cartoon style"], label="video style", info="Please select a video style"),],
                outputs =  ['text',gr.Video()],
                title='Text2VideoEditor',
                allow_flagging="never",
                
            ).launch()
        run_Text2VideoEditor_ui()
    elif args.func == "URL2VideoEditor":
        logger.info('building Text2VideoEditor')
        cfg = get_cfg_defaults()
        # cfg_path = "configs/video_by_retrieval_text_by_chatgpt_zh.yaml"
        cfg.merge_from_file(cfg_path)
        print(cfg)
        editor = build_editor(cfg)
        def run_URL2VideoEditor_logit(input_text, style_text):
            out_video = "test.mp4"
            out_text,video_out = editor.run(input_text,style_text,out_video)
            return out_text,video_out
    
        def run_URL2VideoEditor_ui():
            gr.Interface(
                run_URL2VideoEditor_logit,
                [gr.inputs.Textbox(placeholder="Enter url here...",label='enter url'),  gr.Radio(["realism style", "cartoon style"], label="video style", info="Please select a video style"),],
                outputs =  ['text',gr.Video()],
                title='URL2VideoEditor',
                allow_flagging="never",
                
            ).launch()
        run_URL2VideoEditor_ui()
    
        
