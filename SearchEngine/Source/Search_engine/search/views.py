import hdfs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
import pymongo
from pyspark import SparkContext,SparkConf
import os
redirect
# Create your views here.
def search(request,path):

    conf = SparkConf()
    conf.setMaster('spark://10.2.1.44:7077')
    client_mongo = pymongo.MongoClient(host='10.2.1.60', port=27017)
    client_hdfs = hdfs.Client(url='http://10.2.1.44:50070/', root='/', timeout=10000, session=False)
    os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
    if path=='search/':
        return render(request,'index.html')
    if path=='search/list':
        if request.GET['search']:

            db=client_mongo.search
            search_collection=db.search
            search_content=request.GET['search']
            mongo_content=search_collection.find({'search':search_content}).sort({'click':-1})
            list_data=[]
            if mongo_content:
                for i in mongo_content:
                    url1=i.path
                    title=i.title
                    history_content=i.content
                    list_data.append((url1,title,history_content))
                paginator = Paginator(list_data, 10)
                page = request.GET.get('page')
                try:
                    pages = paginator.page(page)
                except PageNotAnInteger:
                    pages = paginator.page(1)
                except EmptyPage:
                    pages = paginator.page(paginator.num_pages)

                data = {
                    'pages': pages,

                }

                return  render(request,'index1.html',data)
            sc=SparkContext(conf)
            wholetext=sc.textFile('hdfs://10.2.1.44:10000/'+STORAGAGE_PATH).collect()
            for i in wholetext:
                url1=i[1][0]
                title=i[1][1]
                content=i[1][2]
                if search_content in content:
                    index=content.index(search_content)
                    if index<50:
                        content_s=content[0:100]
                    else:
                        content_s=content[index-50:index+50]
                    mongo_content.update({'url':url1},{'$set':{'content':content_s}})
                    list_data.append((url1,title,content_s))
            paginator=Paginator(list_data,10)
            page=request.GET.get('page')
            try:
                pages=paginator.page(page)
            except PageNotAnInteger:
                pages=paginator.page(1)
            except EmptyPage:
                pages=paginator.page(paginator.num_pages)



            data={
                'pages':pages,

            }
            return  render(request,'index1.html',data)
        else :
            db = client_mongo.search
            search_collection = db.search
            mongo_content = search_collection.update({'path': path},{'$inc':{'click':1}})
            url=mongo_content.url
            return redirect(url)











