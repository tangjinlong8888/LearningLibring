import sys
from hdfs.client import Client
def wrtie_to_hdfs(client,hdfs_path,data):
    client.write(hdfs_path,data,overwrite=True,append=False,encoding='utf-8')


def read_hdfs_file(client,filename):
    lines=[]
    with client.read(filename,encoding='utf-8',delimiter='\n' ) as reader:
        for line in reader:
            lines.append(line.strip())
    return lines


def mkdirs(client,hdfs_path):
    client.makedirs(hdfs_path)


def delte_hdfs_file(client,hdfs_path):
    client.delete(hdfs_path)


def put_to_hdfs(client,local_path,hdfs_path):
    client.upload(hdfs_path,local_path,cleanup=True)


def get_from_hdfs(client,hdfs_paht,local_path):
    client.download(hdfs_paht,local_path,overwrite=False)

def append_to_hdfs(client,hdfs_path,data):
    client.write(hdfs_path,data,overwrite=False,append=False,encoding='utf-8')


def write_to_hdfs(client,hdfs_path,data):
    client.write(hdfs_path,data,overwrite=True,append=False,encoding='utf-8')


def mv_or_rename(client,hdfs_src_path,hdfs_dst_path):
    client.rename(hdfs_src_path,hdfs_dst_path)


def list_hdfs_path_name(client,hdfs_path):
    return client.list(hdfs_path,status=False)


def list_hdfs(client,hdfs_path):
    result_list=[]
    path_lsit= client.list(hdfs_path,status=False)
    for i in path_lsit:
        result_list.append(client.resolve(i))
    return result_list


def list_detail_hdfs(client,hdfs_path):
    result_list = []
    path_lsit = client.list(hdfs_path, status=False)
    for i in path_lsit:
        result_list.append(client.resolve(i)+'  type:'+client.status(i)['type'])
    return result_list


if __name__ == '__main__':
    pass

    # client=Client('http://10.2.1.44:50070/',root='/',timeout=10000,session=False)
    # wrtie_to_hdfs(client,'/user/huyang/test_hello.txt','hello,world')
    # print(read_hdfs_file(client,'/user/huyang/test_hello.txt'))
    # print(list_hdfs(client,'/'))
    # print(list_detail_hdfs(client,'/'))
    # print(client.resolve('user'))
    # print(list_hdfs_path_name(client,'/user/huyang'))
    # print(client.status('/'))
    # # print(client.parts('/user/huyang/'))

