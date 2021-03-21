import pymysql
from elasticsearch import Elasticsearch
def get_data():
    conn=pymysql.connect(host="localhost",port=3306,user="root",password="admin",database="freshshop")
    cursor=conn.cursor()
    sql="select * from shop"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.close()
    return results

def create_es_data():
    es=Elasticsearch()
    try:
        results=get_data()
        for row in results:
            print(row)
            message={
                "id":row[0],
                "name":row[1],
                "shop":row[2],
                "category":row[4],
                "price":row[-1]
            }
            es.index(index="freshshop",doc_type="test-type",body=message)
    except Exception as e:
        print("Error:"+str(e))
if __name__=="__main__":
    create_es_data()