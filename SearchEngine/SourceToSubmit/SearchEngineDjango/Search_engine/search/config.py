# -*- coding: utf-8 -*-
#########E.S.P配置文件##########
MONGO_CLIENT = {
    'HOST':'10.2.1.60',
    'PROT':27017,
}
CLIENT_HDFS = {
    'HOST': 'hdfs://10.2.1.44:10000/',
    # 'PROT': 10000,
    'ROOT': '/',
    'SESSION': False,
    'DIR':'search/content',
}
SPARK_MASTER = {
    'HOST': 'spark://10.2.1.44:7077'
}
JAVA_HOME = "/home/sumu/jdk1.8"

PYSPARK_PYTHON = "/usr/bin/python3.4"











































