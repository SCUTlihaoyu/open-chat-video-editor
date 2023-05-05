    
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

def download_video(url):
    urllib_request = urllib.request.Request(
        url,
        data=None,
        headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"},
    )
    with urllib.request.urlopen(urllib_request, timeout=30) as r:
        video_stream = io.BytesIO(r.read())
    return video_stream


class VideoGenByRetrieval(MediaGeneratorBase):
    '''
    generate video by retrieval
    '''
    def __init__(self, config,
                 query_embed_server,
                 index_server,
                 meta_server,
                 ):
        super(VideoGenByRetrieval, self).__init__(config)
        self.config = config
        self.query_embed_server = query_embed_server
        self.index_server = index_server
        self.meta_server = meta_server
        self.tmp_dir = "./tmp/video"
        self.data_type = "video"
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

    def batch_run(self, query:List,**kwargs):
        '''
        run video generator by retrieval
        support multi query
        '''
        assert type(query) == list
    
        # get query embed
        prompt = 'a picture without text'
        query = [ val + prompt for val in query]
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
            # download one of the topk videos
            for url_id,url in enumerate(urls):
                try:
                    video_stream = download_video(url)
                    # try to open
                    url_md5 = self.get_url_md5(url)
                    video_tmp_name = os.path.join(self.tmp_dir, "{}_{}_{}.mp4".format(batch_idx,url_id, url_md5))
                    logger.info('tmp video name: {}'.format(video_tmp_name))
                    with open(video_tmp_name, "wb") as f:
                        f.write(video_stream.getbuffer())
                    one_info = {'url':url,'topk_ids':url_id,'video_local_path':video_tmp_name,'data_type':self.data_type}
                    resp.append(one_info)
                    break
                except Exception as e:
                    logger.error(e)
                    logger.error(traceback.format_exc())
                    
                    continue
        return resp
    