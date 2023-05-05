from yacs.config import CfgNode as CN
_C = CN()
_C.video_editor = CN()
_C.video_editor.type = "Text2Video"


# 视频信息的生成模式
_C.video_editor.visual_gen = CN()
_C.video_editor.visual_gen.type = "image_by_retrieval" 
# 其他类型: image_by_diffusion  video_by_retrieval image_by_retrieval_then_diffusion video_by_diffusion
_C.video_editor.visual_gen.image_by_retrieval = CN()
# query model
_C.video_editor.visual_gen.image_by_retrieval.model = "ViT-L/14" 
_C.video_editor.visual_gen.image_by_retrieval.model_path = ""
_C.video_editor.visual_gen.image_by_retrieval.device = "cpu" # index file path

# index
_C.video_editor.visual_gen.image_by_retrieval.index_path = "" # index file path

# meta
_C.video_editor.visual_gen.image_by_retrieval.meta_path = "" # meta file path


# video query model 
_C.video_editor.visual_gen.video_by_retrieval = CN()
_C.video_editor.visual_gen.video_by_retrieval.model = "ViT-B/32"
_C.video_editor.visual_gen.video_by_retrieval.model_path = ""
_C.video_editor.visual_gen.video_by_retrieval.device = "cpu"

# video index 
_C.video_editor.visual_gen.video_by_retrieval.index_path = ""
_C.video_editor.visual_gen.video_by_retrieval.meta_path = ""


# image gen by diffusion
_C.video_editor.visual_gen.image_by_diffusion = CN()
_C.video_editor.visual_gen.image_by_diffusion.model_id = "stabilityai/stable-diffusion-2-1"

# image_by_retrieval_then_diffusion
_C.video_editor.visual_gen.image_by_retrieval_then_diffusion = CN()

_C.video_editor.visual_gen.image_by_retrieval_then_diffusion.model_id = "stabilityai/stable-diffusion-2-1"





# text gen
_C.video_editor.text_gen = CN()
_C.video_editor.text_gen.type = "toy"
_C.video_editor.text_gen.organization = ""
_C.video_editor.text_gen.api_key = ""

# tts 
_C.video_editor.tts_gen = CN()
_C.video_editor.tts_gen.model = "PaddleSpeechTTS"
# set am
_C.video_editor.tts_gen.am = 'fastspeech2_mix'
_C.video_editor.tts_gen.lang = 'mix'

# subtitle
_C.video_editor.subtitle = CN()
_C.video_editor.subtitle.font=""

# bgm 
_C.video_editor.bgm_gen = CN()
_C.video_editor.bgm_gen.type = "toy"


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()