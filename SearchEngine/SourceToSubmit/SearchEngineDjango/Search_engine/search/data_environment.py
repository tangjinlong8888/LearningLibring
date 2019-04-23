import os
import search.config
from pyspark import SparkContext,SparkConf
import pymongo
os.environ['JAVA_HOME'] = search.config.JAVA_HOME
os.environ["PYSPARK_PYTHON"] = search.config.PYSPARK_PYTHON
conf = SparkConf()
conf.setMaster(search.config.SPARK_MASTER.get('HOST'))
sc = SparkContext(conf=conf)
wholetext_pre = sc.wholeTextFiles(search.config.CLIENT_HDFS.get('HOST') + search.config.CLIENT_HDFS.get('DIR'))
wholetext_pre.persist()
wholetext=wholetext_pre.collect()
client_mongo = pymongo.MongoClient(host=search.config.MONGO_CLIENT.get('HOST'), port=search.config.MONGO_CLIENT.get('PORT'))
db = client_mongo.search_test1
search_collection = db.search_collection1
