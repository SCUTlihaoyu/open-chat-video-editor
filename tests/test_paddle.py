from paddlespeech.cli.tts.infer import TTSExecutor



tts = TTSExecutor()
am = 'speedyspeech_csmsc'
lang = 'zh'
out_path='test1.wav'
text='你好，测试一下数据'
tts(text=text,lang=lang,am=am,output=out_path)