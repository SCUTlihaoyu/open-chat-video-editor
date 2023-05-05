import gradio as gr 

def show_video(input_text,style):
    print(input_text,style)
    return "out text","image_by_retrieval_then_diffusion_chatgpt_zh.mp4"

def run_show_video():
    gr.Interface(
        show_video,
        [gr.inputs.Textbox(placeholder="Enter sentence here..."),  gr.Radio(["realism style", "cartoon style"], label="video style", info="Please select a video style"),],
        outputs =  ['text',gr.Video()],
        title='test',
        allow_flagging="never",

    ).launch()
    
if __name__ == "__main__":
    run_show_video()
    