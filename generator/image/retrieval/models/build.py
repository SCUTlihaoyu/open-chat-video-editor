from comm.mylog import logger
from generator.image.retrieval.models.clip_model import ClipTextEmbed, MClipTextEmbed

def build_image_query_model(model_name, device):
    
    if model_name == "ViT-L/14":
        model = ClipTextEmbed(model_name = model_name, device = device)
    elif model_name == "M-CLIP/XLM-Roberta-Large-Vit-L-14":
        model = MClipTextEmbed(model_name = model_name, device = device)
        
    return model
