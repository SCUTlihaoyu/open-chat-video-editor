# import logging
from generator.image.retrieval.build import build_QueryTextEmbedServer,build_FiassKnnServer
# from generator.image.generation.build import build_img_gen_model
from generator.image.image_generator import ImageGenbyRetrieval,ImageGenByDiffusion,ImageGenByRetrievalThenDiffusion
from generator.comm.meta_sever import ImgMetaServer
from generator.image.generation.build import build_img_gen_model,build_img2img_gen_model
from comm.mylog import logger
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def build_image_generator(cfg):
    '''
    所有的build的入参都是cfg对象
    '''
    image_generator = None
    visual_gen_type = cfg.video_editor.visual_gen.type
    logger.info('visual_gen_type: {}'.format(visual_gen_type))
    if visual_gen_type == "image_by_retrieval":
        logger.info('start build_QueryTextEmbedServer')
        query_model = build_QueryTextEmbedServer(cfg)
        
        # build faiss index 
        logger.info('start build_FiassKnnServer')
        index_server = build_FiassKnnServer(cfg)

        # build meta server 
        logger.info('start build_ImgMetaServer')    
        
        meta_server = ImgMetaServer(cfg.video_editor.visual_gen.image_by_retrieval.meta_path)
    
        image_generator = ImageGenbyRetrieval(cfg,query_model,index_server,meta_server)
    elif visual_gen_type == "image_by_diffusion":
        logger.info("start build_img_gen_model")
        img_gen_model = build_img_gen_model(cfg)
        image_generator = ImageGenByDiffusion(cfg,img_gen_model)
    elif visual_gen_type == "image_by_retrieval_then_diffusion":
        # build img retrieval generator
        logger.info('start build_QueryTextEmbedServer')
        query_model = build_QueryTextEmbedServer(cfg)
        
        # build faiss index 
        logger.info('start build_FiassKnnServer')
        index_server = build_FiassKnnServer(cfg)

        # build meta server 
        logger.info('start build_ImgMetaServer')    
        
        meta_server = ImgMetaServer(cfg.video_editor.visual_gen.image_by_retrieval.meta_path)
    
        image_retrieval_generator = ImageGenbyRetrieval(cfg,query_model,index_server,meta_server)
        img2img_model = build_img2img_gen_model(cfg)
        image_generator = ImageGenByRetrievalThenDiffusion(cfg,image_retrieval_generator,img2img_model)
    else:
        raise ValueError('visual_gen_type: {} not support'.format(visual_gen_type))
    return image_generator