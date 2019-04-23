from django.shortcuts import render
from hdfs import HdfsError

from search.forms import SearchForm
from hdfs.client import Client

# from Python_to_HDFS import get_from_hdfs

# Create your views here.
#
# from pyspark import SparkContext()
# sc=SparkContext()
# textFile=sc.textFile("hdfs://******")
# lines=textFile.filter(lambda line:'**' in line)


def search(request,path):
    # form=SearchForm()
    # data={'form':form}
    # search_data=request.GET['']
    # print(path)
    print(11111111111)
    try:
        client=Client('http://10.2.1.44:50070/',root='/',timeout=10000,session=False)
        client.download('/'+path+'/1.html', 'templates', overwrite=False)
    except HdfsError:
        pass

    print(22222222222222)

    return render(request,'1.html')
