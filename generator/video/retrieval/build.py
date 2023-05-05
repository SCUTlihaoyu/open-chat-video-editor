from generator.video.retrieval.models.build import build_video_query_model
from generator.video.retrieval.server.embed import QueryTextEmbedServer
from generator.video.retrieval.server.knn import VideoFiassKnnServer


def build_QueryTextVideoEmbedServer(cfg):
    model_name = cfg.video_editor.visual_gen.video_by_retrieval.model
    device = cfg.video_editor.visual_gen.video_by_retrieval.device
    
    model = build_video_query_model(model_name = model_name, device = device)
    return QueryTextEmbedServer(model)


def build_VideoFiassKnnServer(cfg):
    index_path = cfg.video_editor.visual_gen.video_by_retrieval.index_path
    return VideoFiassKnnServer(index_path)
