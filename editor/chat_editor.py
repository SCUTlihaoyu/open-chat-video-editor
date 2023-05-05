from comm.mylog import logger
from moviepy.editor import AudioFileClip, VideoFileClip,ImageClip, concatenate_videoclips
from moviepy.editor import TextClip,CompositeVideoClip,CompositeAudioClip
from moviepy.editor import afx
from editor.image_effect import zoom_in_effect



class Text2VideoEditor(object):
    def __init__(self,
                 cfg,
                 text_generator,
                 vision_generator,
                 audio_generator,
                 bgm_generator,
                
                 ) -> None:
        self.text_generator = text_generator
        self.vision_generator = vision_generator
        self.audio_generator = audio_generator
        self.bgm_generator = bgm_generator
        self.cfg = cfg
        # self.style = style
    
    def run(self,input_text,style="",out_file="test.mp4"):
        # setence to passage
        logger.info('input_text: {}'.format(input_text))
        text_resp = self.text_generator.run(input_text)
        text_lang = text_resp['lang']
        if text_lang == 'zh':
            zh_out_text = [val['zh'] for val in text_resp['out_text']]
            logger.info('zh_out_text: {}'.format(zh_out_text))

        en_out_text = [val['en'] for val in text_resp['out_text']]
        # if 
        logger.info('en_out_text: {}'.format(en_out_text))
        # stylized text
        out_text_stylized = [val+','+style for val in en_out_text]
        
        # text 2 voice
        if text_lang == 'zh':
            tts_in_text = zh_out_text
            sub_title_text = zh_out_text
            final_text = zh_out_text
        else:
            tts_in_text = en_out_text
            sub_title_text = en_out_text
            final_text = en_out_text
            
        tts_resp = self.audio_generator.batch_run(tts_in_text)
    
    
        # text 2 vision
        vision_resp = self.vision_generator.batch_run(out_text_stylized)
        
        # merge media 
        final_clips = []
        
        for idx,(tts_info,vision_info,one_text) in enumerate(zip(tts_resp, vision_resp,sub_title_text)):
            audio_file= tts_info['audio_path']
            # load audio
            audio_clip = AudioFileClip(audio_file)
            
            # text clip 
            if self.cfg.video_editor.subtitle.font:
                text_clip = TextClip(one_text, font=self.cfg.video_editor.subtitle.font,fontsize=30, color='black')
            else:
                text_clip = TextClip(one_text,fontsize=30, color='black')
                
            text_clip = text_clip.set_duration(audio_clip.duration)
            vision_type = vision_info['data_type']
            if vision_type == 'image':
                vision_file = vision_info['img_local_path']
                vision_clip = ImageClip(vision_file)
                vision_clip = vision_clip.resize((640,360))
                
                # set duration
                vision_clip = vision_clip.set_duration(audio_clip.duration)
                vision_clip = zoom_in_effect(vision_clip, zoom_ratio=0.04)
                
                vision_clip = vision_clip.set_audio(audio_clip)
            elif vision_type == 'video':
                vision_file = vision_info['video_local_path']
                vision_clip = VideoFileClip(vision_file)
                vision_clip = vision_clip.set_duration(audio_clip.duration)
                vision_clip = vision_clip.resize((640,360))
                vision_clip = vision_clip.set_audio(audio_clip)

            # 
            vision_clip = CompositeVideoClip([vision_clip,text_clip.set_position(('center','bottom'))])
            
            # save for debug 
            vision_clip.write_videofile("test_{}.mp4".format(idx), fps=24)
            final_clips.append(vision_clip)
        logger.info('final_clips: {}'.format(len(final_clips)))
        video = concatenate_videoclips(final_clips)
        
        video_audio = video.audio.volumex(1.0)
        # add bgm 
        bgm_resp = self.bgm_generator.run()
        local_bgm = bgm_resp['bgm_local_file']
        bgm_clip = AudioFileClip(local_bgm).volumex(0.2)
        bgm_clip = afx.audio_loop(bgm_clip,duration=video.duration)
        
        video_audio = CompositeAudioClip([video_audio,bgm_clip])
        
        # add audio and bgm 
        video = video.set_audio(video_audio)
        
        video.write_videofile(out_file, fps=24)
        
        return final_text, out_file




