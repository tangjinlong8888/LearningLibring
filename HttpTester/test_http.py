import json
import re
from tabulate import tabulate


# 接口类
class Interface(object):

    # 初始化url
    def __init__(self, url):
        self.url = url
        self.requests_list = []

    # 添加请求request
    def add_request(self, request):
        self.requests_list.append(request)

    # 测试
    def test(self):
        for request in self.requests_list:
            try:
                request.request(self.url)
                yield self.url, request.method, True, None
            except Exception as e:
                yield self.url, request.method, False, e

            # 判断request的请求方法
            # if request.attrib['method'] == 'get':
            #     # get请求url的响应
            #     http_response = requests.get(self.url, params=None)
            #     # 打印出当前状态码
            #
            #     # 判断状态码
            #     if http_response.status_code == 200:
            #         # 返回预期的格式是什么
            #         if re.type == 'json':
            #             try:
            #                 # 将json格式转换为字典格式
            #                 data = json.loads(http_response.text)
            #                 # 验证字段是否与预期符合
            #                 filde.validate_json(data)
            #                 yield self.url, http_response.status_code, request.attrib['method'], True, None
            #                 # table = [['url','status_code', 'method', 'results'], [self.url,http_response.status_code,
            #                 #                                                 request.attrib['method'], '成功']]
            #                 # print(tabulate(table))
            #
            #             except Exception as e:
            #                 yield self.url, http_response.status_code, request.attrib['method'], False, e
            #                 #
            #                 # table = [['url','status_code', 'method', 'results'],
            #                 #          [self.url,http_response.status_code, request.attrib['method'], e]]
            #                 # print(tabulate(table))
            #
            #         if re.type == 'text':
            #             try:
            #                 data = http_response.text
            #                 filde.validate_text(data)
            #             except Exception as e:
            #                 print('请求方式：{},验证失败：{}'.format(request.attrib['method'], e))
            #
            #     if http_response.status_code == 302:
            #         raise ConnectionRefusedError('服务重定向:{}'.format(http_response.status_code))
            #     if http_response.status_code == 403:
            #         raise ConnectionRefusedError('请求错误{}'.format(http_response.status_code))
            #     if http_response.status_code == 503:
            #         raise ConnectionRefusedError('服务端错误{}'.format(http_response.status_code))

            # if request.attrib['method'] == 'post':
            #     # post请求字段
            #     data = rq.arguments
            #     # post请求url的响应
            #     http_response = requests.post(self.url, json=data)
            #     # 打印当前状态码
            #
            #     if http_response.status_code == 200:
            #         if re.type == 'json':
            #             try:
            #                 data = json.loads(http_response.text)
            #                 filde.validate_json(data)
            #                 yield self.url, http_response.status_code, request.attrib['method'], True, None
            #                 # table = [['url', 'status_code', 'method', 'results'], [self.url,http_response.status_code,
            #                 #                                                 request.attrib['method'], '成功']]
            #                 # print(tabulate(table))
            #             except Exception as e:
            #                 yield self.url, http_response.status_code, request.attrib['method'], False, e
            #                 # table = [['url','status_code', 'method', 'results'], [self.url,http_response.status_code,
            #                 #                                                 request.attrib['method'], e]]
            #                 # print(tabulate(table))
            #
            #         if re.type == 'text':
            #             data = http_response.text
            #             filde.validate_text(data)
            #             print('请求方式为{},返回数据为{}'.format(request.attrib['method'], data))
            #     if http_response.status_code == 302:
            #         raise ConnectionRefusedError('服务重定向{}'.format(http_response.status_code))
            #     if http_response.status_code == 403:
            #         raise ConnectionRefusedError('请求错误{}'.format(http_response.status_code))
            #     if http_response.status_code == 503:
            #         raise ConnectionRefusedError('服务端错误{}'.format(http_response.status_code))


# 请求类
class Request(object):
    def __init__(self, method):
        self.method = method
        self.arguments = []
        self.response_validator = None




    # 添加字段
    def add_argument(self, arg):
        self.arguments.append(arg)

    # 测试阶段
    def request(self, url):
        import requests
        arguments = {}
        for arg in self.arguments:
            arguments[arg.name] = eval(arg.type)(arg.value)

        if self.method == "get":
            http_response = requests.request(self.method, url, data=arguments)
        elif self.method == "post":
            http_response = requests.request(self.method, url, json=arguments)
        else:
            raise NotImplementedError('暂不支持该方法')
        if http_response.status_code == 200:

            self.response_validator.validate(http_response)

        if http_response.status_code == 302:
            raise ConnectionRefusedError('服务重定向{}'.format(http_response.status_code))
        if http_response.status_code == 403:
            raise ConnectionRefusedError('请求错误{}'.format(http_response.status_code))
        if http_response.status_code == 503:
            raise ConnectionRefusedError('服务端错误{}'.format(http_response.status_code))


# 响应类
class Response(object):
    def __init__(self, content_type, response_data):
        try:
            assert content_type in ("json", "text")
        except Exception as e:
            raise TypeError('没有该类型{}'.format(e))
        self.response_data = response_data
        self.content_type = content_type

    # 验证类型
    def validate(self, response):

        # 头部字段
        content_type = response.headers['Content-Type']
        # 判断头部是否是text格式
        if self.content_type == "text":
            import re
            # 验证text返回

            if not re.match(self.response_data.strip(), response.text):
                raise TypeError("返回不正确")

        # 判断头部是否是json格式
        if self.content_type == "json":
            if content_type != 'application/json':
                raise TypeError("类型不正确")
            return_data = json.loads(response.text)
            for field in self.response_data:
                field.validate_json(return_data)

# 字段类
class Field(object):
    def __init__(self, name, type, required=False, value=None):
        self.name = name
        self.type = type
        self.required = required
        self.value = value

    # 验证json格式字段
    def validate_json(self, data):

        if self.required and self.name not in data.keys():
            raise ValueError('The lack of items:{}'.format(self.name))

        if not isinstance(data[self.name], eval(self.type)):
            raise TypeError('Incorrect type:{}'.format(self.type))

        if self.type == "str":
            if not re.match(self.value, data[self.name]):
                raise ValueError('Incorrect data：{}'.format(data[self.name]))
        elif self.type in ("int", "float"):

            if int(self.value) != int(data[self.name]):
                raise ValueError('{} int Incorrect data：{}'.format(self.value, data[self.name]))

    #
    # # 验证text格式字段
    # def validate_text(self, data):
    #     if not re.match(self.value, data):
    #         raise ValueError('数据不正确')


# 测试类
class Tester(object):
    def __init__(self, path):
        self.interfaces = []
        self.parse_xml(path)

    # 解析xml 获取所有属性
    def parse_xml(self, path):
        from lxml import etree
        tree = etree.parse(path)
        root = tree.getroot()

        # 判断节点是否为http
        if root.tag != 'http':
            raise TypeError('Parse failed')

        # 遍历http下所有节点
        for interface in root:
            # 获取interface属性
            inf = Interface(interface.attrib['url'])
            # 遍历interface下所有节点
            for request in interface:
                # 判断节点是否为renquest
                if request.tag == "request":
                    # 获取request方法并new一个Request
                    req = Request(request.attrib['method'])
                    # 找到request下所有节点
                    for itr in request:
                        # 判断节点是否为argument
                        if itr.tag == "argument":
                            # 找到argument下所有节点
                            for field in itr:
                                # 判断节点是否为field
                                if field.tag != "field":
                                    continue
                                # new一个Field
                                f = Field(name=field.attrib['name'], type=field.attrib['type'],
                                          value=field.attrib['value'])
                                req.add_argument(f)
                        # 判断节点是否为response
                        elif itr.tag == "response":
                            # 判断节点属性是否为json
                            if itr.attrib['type'] == "json":
                                response_data = []
                                # 找到response下所有节点
                                for field in itr:
                                    # 判断节点是否为field
                                    if field.tag != "field":
                                        continue
                                    f = Field(name=field.attrib['name'],
                                              type=field.attrib['type'],
                                              value=field.attrib['value'],
                                              required=field.attrib['required'])
                                    response_data.append(f)
                            else:
                                # 节点属性为text
                                response_data = itr.text

                            resp = Response(itr.attrib['type'], response_data)
                            req.response_validator = resp

                    # 请求添加到request
                    inf.add_request(req)
            # interface添加
            self.interfaces.append(inf)

            # t.add_request(art)
            #
            # # 获取request属性
            # req = art.attrib['method']
            # rq = Request(req)
            #
            # # 遍历request下所有节点
            # for arg in art:
            #     # 判断节点是否为argument
            #     if arg.tag == 'argument':
            #
            #         # 遍历arg下所有节点
            #         for filed in arg:
            #             if filed is not None and filed.tag=='field':
            #                 # 获取节点所有属性
            #                 name = filed.attrib['name']
            #                 type = filed.attrib['type']
            #                 value = filed.attrib['value']
            #                 rq.add_argument(name, value, type)
            #
            #     # 判断节点是否为response
            #     if arg.tag == 'response':
            #         # 获取节点的type属性
            #         res = arg.attrib['type']
            #         re = Response(res)
            #         if res == 'json':
            #             # 遍历arg下所有节点
            #
            #             for filed in arg:
            #                 re.add_fild(filed)
            #                 if filed.tag=='field':
            #
            #                     # 获取节点所有属性
            #                     name = filed.attrib['name']
            #                     type = filed.attrib['type']
            #                     required = filed.attrib['required']
            #                     value = filed.attrib['value']
            #                     F = Field(name, type, required, value)
            #             t.test(F, re, rq)
            #
            #             self.interfaces.pop()

    def do_test(self):
        for inf in self.interfaces:
            for url, method, result, reason in inf.test():
                yield url, method, result, reason


if __name__ == '__main__':
    import sys
    t = Tester(sys.argv[1])
    tables = []

    # t=Tester('/Users/admin/Desktop/untitled1/P1806/projects/document/Automated_test/config.xml')
    for url, method, request, reason in t.do_test():
        tables.append((url, method, request, reason))
    import tabulate

    # 打印出表格形式
    print(tabulate.tabulate(tables, headers=("URL", 'METHOD', 'RESULT', 'REASON')))
