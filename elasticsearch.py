from elasticsearch import E

es=Elasticsearch()
# 添加数据
es.index(index="my_index",doc_type="test_type",id=1,body={"name":"python","addr":"深圳"})
# 查询数据
result = es.search(index="my_index",doc_type="test_type")
# 打印所有数据
for item in result["hits"]["hits"]:
    print(item["_source"])
