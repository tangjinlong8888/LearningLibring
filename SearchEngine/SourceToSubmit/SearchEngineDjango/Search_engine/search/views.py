
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

import os
# Create your views here.
from search.data_environment import wholetext,search_collection
search_collection=search_collection # the table from mongodb
wholetext=wholetext  # the collection of data from the hadoop

def search(request):
    """
    the search_home page
    :param request:
    :return:
    """
    return render(request, 'index.html')


@cache_page(60*15,key_prefix='site1') # cache the templates for 15min
def detail(request):
    """
    return the page that match your searching
    :param request:
    :return:
    """
    search_content = request.GET['search'] # get the search key

    global search_collection # make the table a global var
    mongo_content=search_collection.find({'search_content':search_content}).sort([('click',-1)])
    # search from the mongodb
    list_data=[]
    # a list to store the  data
    b=list(mongo_content)
    if  b:
        for i in b:
            id=i.get('_id') # get the id from dbs
            title=i.get('title') # get the title from dbs
            history_content=i.get('content') # get the content from dbs
            list_data.append((id,title,history_content)) # add the data tuple to the list_data
        paginator = Paginator(list_data, 10)
        # initialize the paginator and set 10 items per page and the total data that match the case
        page = request.GET.get('page')
        # get the page from the request
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        # deal with the exception of empty and the page number is not a int number
        data = {
            'pages': pages,
            'search': request.GET['search']
        }
        return  render(request,'index1.html',data)
        # return and use the page render the html files
    global wholetext
    # make the wholetext a global var
    for i in wholetext:
        """
        the data in the wholetext is a list that composed with tuple,the first element in the element is the name 
        of file ,and the second is the content ,whose first line is url and second line is title about the article 
        """
        b=i[1].split('\n',2)
        url1=b[0]  # url
        title=b[1] # title
        content=b[2] # content
        if search_content in content:
            index=content.index(search_content)
            if index<100:
                content_s=content[0:100]
                # get the content that about the search key
            else:
                content_s=content[index-100:index+100]
                # get the content that about the search key
            search_collection.update({'url':url1},{'$set':{'content':content_s}})
            # update the content that in mongodb
            search_collection.update({'url':url1},{'$set':{'search_content':search_content}})
            # update the search key that in mongodb
            id=list(search_collection.find({'url':url1}))[0].get('_id')
            list_data.append((id,title,content_s))
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
        'search':request.GET['search']
    }
    return  render(request,'index1.html',data)

def jump(request,path):
    """
    the function that record the click and redirect the response url
    :param request:
    :param path:
    :return:
    """
    search_collection.update({'_id': int(path)},{'$inc':{'click':1}})
    # to add 1 at the click content
    mongo_content=search_collection.find({'_id': int(path)})
    # get the url
    b=list(mongo_content)
    url=b[0].get('url')
    return redirect(url)
# redirect the respond url
