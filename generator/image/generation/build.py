from generator.image.generation.stable_diffusion import StableDiffusionImgModel,StableDiffusionImg2ImgModel

def build_img_gen_model(cfg):
    
    model_id = cfg.video_editor.visual_gen.image_by_diffusion.model_id
    model = StableDiffusionImgModel(model_id)
    return model

def build_img2img_gen_model(cfg):
    model_id = cfg.video_editor.visual_gen.image_by_retrieval_then_diffusion.model_id
    model = StableDiffusionImg2ImgModel(model_id)
    return model