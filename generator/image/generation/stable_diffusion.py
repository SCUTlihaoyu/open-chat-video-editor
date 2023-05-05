
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler,StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
class StableDiffusionImgModel(object):
    def __init__(self,model_id="stabilityai/stable-diffusion-2-1") -> None:
        self.model_id = model_id
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
        self.pipe = self.pipe.to("cuda")
    
    def run(self,prompt):
        image = self.pipe(prompt).images[0]
        width, height = image.size
        new_width = 640
        new_height = 360
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2
        # Crop the center of the image
        image = image.crop((left, top, right, bottom))
        
        return image

class StableDiffusionImg2ImgModel(object):
    def __init__(self,model_id="stabilityai/stable-diffusion-2-1") -> None:
        self.model_id = model_id 
        self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")

    def run(self,prompt,init_image_path):
        init_image = Image.open(init_image_path).convert('RGB')
        init_image = init_image.resize((768, 768))
        image = self.pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5,num_inference_steps=100).images[0]
        width, height = image.size
        new_width = 640
        new_height = 360
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2
        # Crop the center of the image
        image = image.crop((left, top, right, bottom))
        return image
