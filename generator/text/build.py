# import logging
from comm.mylog import logger
from generator.text.models.toy import EnToyTextGenModel, ZhToyTextGenModel,ZhToyURL2TextModel
from generator.text.models.chatgpt import ChatGPTModel,URL2TextChatGPTModel


def build_text_generator(cfg):
    text_gen_type = cfg.video_editor.text_gen.type
    logger.info('text_gen_type: {}'.format(text_gen_type))
    text_generator = None
    if text_gen_type == "EnToyTextGenModel":
        text_generator = EnToyTextGenModel()
    elif text_gen_type == "ZhToyTextGenModel":
        text_generator = ZhToyTextGenModel()
    elif text_gen_type == "ZhToyURL2TextModel":
        text_generator = ZhToyURL2TextModel()
        
    elif text_gen_type == "ChatGPTModel":
        organization = cfg.video_editor.text_gen.organization
        api_key = cfg.video_editor.text_gen.api_key
        text_generator = ChatGPTModel(cfg,organization,api_key)
    elif text_gen_type == "URL2TextChatGPTModel":
        organization = cfg.video_editor.text_gen.organization
        api_key = cfg.video_editor.text_gen.api_key
        text_generator = URL2TextChatGPTModel(cfg,organization,api_key)
        
    
    return text_generator
