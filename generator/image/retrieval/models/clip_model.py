import clip
from multilingual_clip import pt_multilingual_clip
import transformers
import torch
import numpy as np


def build_clip_model(model_name = "Vit-L/14", device="cpu"):
    model, preprocess = clip.load(model_name, device = device)
    return model,preprocess, lambda t: clip.tokenize(t, truncate=True)


def build_mclip_model(model_name = "M-CLIP/XLM-Roberta-Large-Vit-L-14", device="cpu"):
    model = MClip(model_name,device)
    return model,None,model.get_tokenizer

class ClipTextEmbed(object):
    def __init__(self,model_name,device) -> None:
        self.model_name = model_name
        self.device = device
        self.model, self.preprocess, self.tokenizer = build_clip_model(model_name = model_name, device = device)
        self.model.eval()
    def get_text_embed(self,text):
        '''
        text：list[str]
        '''
        assert type(text) == list
        text = self.tokenizer(text)
        
        with torch.no_grad():
            query_features = self.model.encode_text(text)
        # norm
        query_features /= query_features.norm(dim=-1, keepdim=True)
        query_features = query_features.cpu().to(torch.float32).detach().numpy()

        return query_features
        
        
class MClipTextEmbed(object):
    def __init__(self,model_name,device) -> None:
        self.model_name = model_name
        self.device = device
        self.model = pt_multilingual_clip.MultilingualCLIP.from_pretrained(model_name)
        self.model.eval()
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    

    
    def get_text_embed(self,text):
        '''
        text：list[str]
        '''
        assert type(text) == list
        with torch.no_grad():
            embed = self.model.forward(text, self.tokenizer).detach().cpu().numpy()
        # l2 norm 
        embed = embed / np.linalg.norm(embed, ord=2 ,axis=1, keepdims=True)
        return embed


def test_mclip():

    model = MClip("M-CLIP/XLM-Roberta-Large-Vit-L-14","cpu")
    text = ["hello world","你好"]
    embed = model.get_text_embed(text)
    print(embed.shape)

if __name__ == "__main__":
    test_mclip()