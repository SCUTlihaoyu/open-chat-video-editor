import torch
import logging

class QueryTextEmbedServer(object):
    '''
    query text -> embed
    '''
    def __init__(self,model):
        self.model = model
 
    
    def get_query_embed(self,query):
        '''
        query: str
        support batch
        '''
        query_features = self.model.get_text_embed(query)
 

        return query_features
    
    