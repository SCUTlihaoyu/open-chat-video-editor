from paddlespeech.cli.tts.infer import TTSExecutor
from comm.mylog import logger

class PaddleSpeechTTS(object):
    def __init__(self,
                 lang='mix',
                 am='fastspeech2_mix',
                 ) -> None:
        self.tts = TTSExecutor()
        self.am = am
        self.lang = lang
        logger.info('building PaddleSpeechTTS, am: {}, lang: {}'.format(am,lang))
        
    
    def run_tts(self,text,out_path):
        self.tts(text=text,lang=self.lang,am=self.am,output=out_path)
    