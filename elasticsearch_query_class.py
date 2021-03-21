from elasticsearch import Elasticsearch
class elasticsearch():
    def __init__(self,index_name,index_type):
        self.es=Elasticsearch();
        self.index_name=index_name
        self.index_type=index_type
    def search(self,query,count:int=30):
        ds1={
            "query":{
                "multi_match":{
                    "query":query,
                    "fields":["name","shop"]
                }
            }
        }
        match_data=self.es.search(index=self.index_name,doc_type=self.index_type,body=ds1,size=count)
        return match_data