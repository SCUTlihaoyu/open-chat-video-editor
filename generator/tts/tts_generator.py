from generator.comm.media_generator import MediaGeneratorBase
import os
class TTSGenerator(MediaGeneratorBase):
    def __init__(self, config,
                 tts_model = None,
                 ) -> None:
        super().__init__(config)
        self.tmp_dir = './tmp/tts'
        self.tts_model = tts_model
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
    def run_tts(self,text):
        
        out_path = os.path.join(self.tmp_dir,self.get_str_md5(text)+'.wav')
        self.tts_model.run_tts(text,out_path)
        resp = {'audio_path':out_path}
        return resp 
    
    def batch_run(self,text_list):
        '''
        text_list: [text1,text2,...]
        return:[{'audio_path':audio_path1},{'audio_path':audio_path2},...]
        '''
        assert type(text_list) == list
        resp = []
        for text in text_list:
            resp.append(self.run_tts(text))
        return resp
            
        