from flask import Flask,request
from elasticsearch_query_class import elasticsearch
import json
app=Flask(__name__)
@app.route("/")
def index():
    return "Hello World"
@app.route("/get_es/<query>")
def get_es(query):
    es=elasticsearch(index_name="freshshop",index_type="test-type")
    data=es.search(query)
    print(data)
    address_data=data["hits"]["hits"]
    address_list=[]
    for item in address_data:
        address_list.append(item["_source"])
    new_json=json.dumps(address_list,ensure_ascii=False)
    return app.response_class(new_json,content_type="application/json")
if __name__=="__main__":
    app.run(threaded=True)