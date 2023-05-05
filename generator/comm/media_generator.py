import os 
import hashlib
class MediaGeneratorBase(object):
    '''
    各种媒体的生成器基类
    '''
    def __init__(self,config) -> None:
        self.config = config
    def run(self, **kwargs):
        '''
        生成器的入口函数
        '''
        raise NotImplementedError
    
    def get_url_md5(self,url):
        '''
        获取url的md5值
        '''
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        return m.hexdigest()
    
    def get_pil_md5(self,img):
        md5 = hashlib.md5(img.tobytes()).hexdigest()
        return md5
    

    def get_str_md5(self,str_val):
        '''
        获取字符串的md5值
        '''
        m = hashlib.md5()
        m.update(str_val.encode('utf-8'))
        return m.hexdigest()