from generator.image.retrieval.models.build import build_image_query_model
from generator.image.retrieval.server.embed import QueryTextEmbedServer
from generator.image.retrieval.server.knn import FiassKnnServer
from comm.mylog import logger

def build_QueryTextEmbedServer(cfg):
    model_name = cfg.video_editor.visual_gen.image_by_retrieval.model
    device = cfg.video_editor.visual_gen.image_by_retrieval.device
    
    model = build_image_query_model(model_name = model_name, device = device)
    return QueryTextEmbedServer(model)



def build_FiassKnnServer(cfg):
    index_path = cfg.video_editor.visual_gen.image_by_retrieval.index_path
    return FiassKnnServer(index_path)


    


