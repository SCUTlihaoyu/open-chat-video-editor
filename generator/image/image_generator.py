# 在这里实现基于检索和基于生成的外部接口逻辑

from generator.comm.media_generator import MediaGeneratorBase
import urllib
import urllib.request
import io
import traceback
import os
from PIL import Image
from typing import List
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
from comm.mylog import logger
def download_image(url):
    urllib_request = urllib.request.Request(
        url,
        data=None,
        headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"},
    )
    with urllib.request.urlopen(urllib_request, timeout=10) as r:
        img_stream = io.BytesIO(r.read())
    return img_stream



class ImageGenbyRetrieval(MediaGeneratorBase):
    '''
    generate image by text retrieval
    
    '''
    def __init__(self, config,
                    query_embed_server,
                    index_server,
                    meta_server,
                 ):
        super(ImageGenbyRetrieval, self).__init__(config)
        self.config = config
        self.query_embed_server = query_embed_server
        self.index_server = index_server
        self.meta_server = meta_server
        self.tmp_dir = "./tmp/image"
        self.data_type = "image"

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
        
        
    def batch_run(self, query:List,**kwargs):
        '''
        run image generator by retrieval
        support multi query
        '''
        assert type(query) == list
        prompt = 'a picture without text'
        query = [ val + prompt for val in query]
        # get query embed
        query_embed = self.query_embed_server.get_query_embed(query)
        
        # knn search, indices: [batch_size, top_k]
        distances, indices = self.index_server.search(query_embed)

        # get meta 
        resp = []
        for batch_idx,topk_ids in  enumerate(indices):
            # one_info = {}
            # one query topk urls
            urls = self.meta_server.batch_get_meta(topk_ids) 
            # logging.error('urls: {}'.format(urls))
            # download one of the topk images
            for url_id,url in enumerate(urls):
                
                try:
                    img_stream = download_image(url)
                    # try to open
                    url_md5 = self.get_url_md5(url)
                    img_tmp_name = os.path.join(self.tmp_dir, "{}_{}_{}.jpg".format(batch_idx,url_id, url_md5))
                    logger.info('tmp img name: {}'.format(img_tmp_name))
                    img = Image.open(img_stream).convert('RGB')
                    img.save(img_tmp_name)
                    one_info = {'url':url,'topk_ids':url_id,'img_local_path':img_tmp_name,'data_type':self.data_type}
                    resp.append(one_info)
                    break
                
                except Exception as e:
                    logger.error(e)
                    logger.error(traceback.format_exc())
                    
                    continue
        
                
    
        return resp
    
    
        
        
class ImageGenByDiffusion(MediaGeneratorBase):
    '''
    generate image by stable diffusion
    '''
    def __init__(self, config,
                 img_gen_model,
                 ):
        super(ImageGenByDiffusion, self).__init__(config)
        self.config = config
        self.img_gen_model = img_gen_model
        self.tmp_dir = "./tmp/image"
        self.data_type = "image"
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
            
    def batch_run(self, query:List,**kwargs):

        assert type(query) == list
        resp = []
        for idx,text in enumerate(query):
            img = self.img_gen_model.run(text)
            pil_md5 = self.get_pil_md5(img)
            img_tmp_name = os.path.join(self.tmp_dir, "{}_{}.jpg".format(idx,pil_md5))
            img.save(img_tmp_name)
            one_info = {'img_local_path':img_tmp_name,'data_type':self.data_type}
            resp.append(one_info)
        return resp
    
            
        
    
    
    


class ImageGenByRetrievalThenDiffusion(MediaGeneratorBase):
    '''
    generate image by retrieval then stable diffusion
    '''
    def __init__(self, config,
                    img_gen_by_retrieval_server,
                    img_gen_model,
                    ):
        super(ImageGenByRetrievalThenDiffusion, self).__init__(config)
        self.config = config
        self.img_gen_by_retrieval_server = img_gen_by_retrieval_server
        self.img_gen_model = img_gen_model
        
    def batch_run(self, query, **kwargs):
        '''
        run image generator by retrieval the diffusion
        '''
        assert type(query) == list

        # (1) img retrieval
        retrieval_resp_list = self.img_gen_by_retrieval_server.batch_run(query)
        
        # (2) img2img by diffusion
        for text,item in  zip(query,retrieval_resp_list):
            local_img_path = item["img_local_path"]
            img = self.img_gen_model.run(text,local_img_path)
            # save back 
            img.save(local_img_path)
        return retrieval_resp_list
    
