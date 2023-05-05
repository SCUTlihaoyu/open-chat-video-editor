import dbm 
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class MetaServerBase(object):
    def get_meta(self,ids):
        raise NotImplementedError


class ImgMetaServer(MetaServerBase):
    def __init__(self,db_path) -> None:
        
        logging.info('db_path: {}'.format(db_path))
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        ids = str(ids)
        url = self.db[ids].decode('utf-8')
        return url
    
    def batch_get_meta(self,ids_list):
        
        urls = [self.db[str(idx)].decode('utf-8') for idx in ids_list]
        return urls 

    
class VideoMetaServer(MetaServerBase):
    def __init__(self,db_path) -> None:
        
        logging.info('db_path: {}'.format(db_path))
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        ids = str(ids)
        url = self.db[ids].decode('utf-8')
        return url
    
    def batch_get_meta(self,ids_list):
        
        urls = [self.db[str(idx)].decode('utf-8') for idx in ids_list]
        return urls 

        
        
    