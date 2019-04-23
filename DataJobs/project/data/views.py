from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
from good import dq_user
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/spider')
# engine = create_engine('mysql+pymysql://admin:123456@192.168.2.104:3306/zl_db')




def get_test_page(request):
    # print('hello')
    return render(request, 'bar-tick-align.html', {'order': dq_user.dq_user()})


def get_map_page(request):
    return render(request, 'map-polygon.html', {'order': dq_user.dq_user()})


def get_hist_page(request):
    return render(request, 'dataset-series-layout-by.html', {'order': dq_user.dq_user()})


def get_pie_page(request):
    return render(request, 'pie-pattern.html', {'order': dq_user.dq_user()})


def get_line_page(request):
    return render(request, 'line-stack.html', {'order': dq_user.dq_user()})

def get_knn_page(request):
    return render(request, 'knn.html', {'order': dq_user.dq_user()})

def get_test_data(request):
    data = [300, 520, 200, 334, 390, 330, 220]
    return JsonResponse({'data': data})


def get_knn_data(request):
    sql = 'select money,city_code,edulevel_code,workingexp_code from python'

    df = pd.read_sql_query(sql, engine)

    # 得到数据中没有具体薪资范围的行号的列表
    rows = [x for x in range(len(df.values)) if '-' not in df.values[x][0]]
    # 删除数据中没有具体薪资范围的行
    df = df.drop(rows, inplace=False)
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    # print(df)

    money_count = pd.value_counts(df['money'])
    money_count = money_count[money_count > 100]
    print(money_count.index)
    # print(df.values[1][0])

    rows = [x for x in range(len(df.values)) if df.values[x][0] not in list(money_count.index)]
    # print(rows)
    df = df.drop(rows, inplace=False)
    df = df.reset_index()
    df = df.drop(['index'], axis=1)

    # 取出目标值（标签lable）
    y = df['money']
    # 取出特征值
    x = df.drop(['money'], axis=1)

    # 进行数据的分割，分成训练集和测试集
    test_size = 0.2
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

    # 特征工程（标准化）
    # std = StandardScaler()
    #
    # x_train = std.fit_transform(x_train)
    #
    # x_test = std.fit_transform(x_test)

    data = {}
    data['total'] = len(x)
    data['test_size'] = str(test_size*100)+'%'
    # 进行算法流程(fit,predict,score)
    k = request.POST.get('knum',20)
    knn_list = []
    for i in range(5, int(k)+1):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)

        # 得出预测结果
        y_predict = knn.predict(x_test)

        # 计算准确率
        score = knn.score(x_test, y_test)
        temp = {}
        temp['k'] = i
        temp['score'] = score
        knn_list.append(temp)

    data['knn'] = knn_list

    return JsonResponse(data)


def get_query_data(request):
    sql = 'select city,edulevel,workingexp from python'

    df = pd.read_sql_query(sql,engine)
    city = pd.value_counts(df['city'])
    edulevel = pd.value_counts(df['edulevel'])
    workingexp = pd.value_counts(df['workingexp'])
    data = {'city':list(city.index),'edulevel':list(edulevel.index),'workingexp':list(workingexp.index)}

    return JsonResponse(data)


def get_line_data(request):
    city = request.POST.get('city','成都')
    edulevel = request.POST.get('edulevel','不限')
    workingexp = request.POST.get('workingexp','不限')
    item = request.POST.get('item','python')

    sql = 'select money from {} where city="{}" and edulevel="{}" and workingexp="{}"'.format(item,city,edulevel,workingexp)

    print(sql)
    df = pd.read_sql_query(sql, engine)
    # 得到数据中没有具体薪资范围的行号的列表
    rows = [x for x in range(len(df.values)) if '-' not in df.values[x][0]]
    # 删除数据中没有具体薪资范围的行
    df = df.drop(rows, inplace=False)
    # 将薪资字符串转换为数值类型，只取薪资范围里面的最小值，例如8K-10K，取8000
    salary = {'min': [], 'max': []}
    salary['index'] = [i for i in range(len(df))]
    for i in range(len(df.values)):
        salary['min'].append(float(df.values[i][0].split('-')[0].replace('K', '')) * 1000)
        salary['max'].append(float(df.values[i][0].split('-')[1].replace('K', '')) * 1000)
    cut_num = len(salary['min'])//20
    minlist = sorted(salary['min'])[cut_num:len(salary['min'])-cut_num]
    maxlist = sorted(salary['max'])[cut_num:len(salary['max'])-cut_num]
    if len(minlist) != 0 and len(maxlist) != 0:
        min_mean = int(sum(minlist)/len(minlist))
        max_mean = int(sum(maxlist)/len(maxlist))
        salary['salary'] = str(min_mean)+'-'+str(max_mean)+'元/月'
    else:
        salary['salary'] = '未查询到相关数据！'

    return JsonResponse(salary)


def get_pie_data(request):
    item = request.POST.get('item','python')
    sql = 'select companysize,companytype,edulevel,workingexp from {}'.format(item)
    df = pd.read_sql_query(sql, engine)
    # print(df.head(1))
    # print(df.info())
    # 统计企业规模
    for i in range(len(df['companysize'])):
        if df['companysize'][i] == '':
            df['companysize'][i] = '不限'
    companysize_data = pd.value_counts(df['companysize'])
    # 统计企业类别
    companytype_data = pd.value_counts(df['companytype'])
    # 统计教育水平
    for i in range(len(df['edulevel'])):
        if df['edulevel'][i] == '':
            df['edulevel'][i] = '不限'
    edulevel_data = pd.value_counts(df['edulevel'])
    # 统计工作年限
    for i in range(len(df['workingexp'])):
        if df['workingexp'][i] == '':
            df['workingexp'][i] = '不限'
    workingexp_data = pd.value_counts(df['workingexp'])

    # 格式化数据
    data = {}
    # 格式化公司规模数据
    templist = []
    for i in range(len(companysize_data)):
        tempdict = {}
        tempdict['value'] = int(companysize_data[i])
        tempdict['name'] = companysize_data.index[i]
        templist.append(tempdict)
    # print(templist)
    data['companysize'] = templist
    templist = []

    # 格式化公司类型数据
    for i in range(len(companytype_data)):
        tempdict = {}
        tempdict['value'] = int(companytype_data[i])
        tempdict['name'] = companytype_data.index[i]
        templist.append(tempdict)
    # print(templist)
    data['companytype'] = templist
    templist = []

    # 格式化教育水平数据
    for i in range(len(edulevel_data)):
        tempdict = {}
        tempdict['value'] = int(edulevel_data[i])
        tempdict['name'] = edulevel_data.index[i]
        templist.append(tempdict)
    # print(templist)
    data['edulevel'] = templist
    templist = []

    # 格式化工作年限数据
    for i in range(len(workingexp_data)):
        tempdict = {}
        tempdict['value'] = int(workingexp_data[i])
        tempdict['name'] = workingexp_data.index[i]
        templist.append(tempdict)
    # print(templist)
    data['workingexp'] = templist

    return JsonResponse(data)


def get_hist_data(request):
    item = request.POST.get('item','python')
    sql = 'select money,city from {}'.format(item)
    # 读取数据库数据，得到DataFrame
    df = pd.read_sql_query(sql, engine)
    # 得到数据中没有具体薪资范围的行号的列表
    rows = [x for x in range(len(df.values)) if '-' not in df.values[x][0]]
    # 删除数据中没有具体薪资范围的行
    df = df.drop(rows, inplace=False)
    # 将薪资字符串转换为数值类型，只取薪资范围里面的最小值，例如8K-10K，取8000
    for i in range(len(df.values)):
        df.values[i][0] = float(df.values[i][0].split('-')[0].replace('K', '')) * 1000
    # 获取城市名字，做序列化，将数据转换为前端需要的数据样式
    cities = list(pd.value_counts(df['city'].T).index)
    line = ['city', '5K以下', '5K-10K', '10K-15K', '15K-20K', '20K以上']
    data = [line]
    for i in cities:
        temp = []
        his_dict = {'5K以下': 0, '5K-10K': 0, '10K-15K': 0, '15K-20K': 0, '20K以上': 0}
        for j in range(len(df.values)):
            if df.values[j][1] == i:
                if df.values[j][0] < 5000:
                    his_dict['5K以下'] += 1
                elif df.values[j][0] < 10000:
                    his_dict['5K-10K'] += 1
                elif df.values[j][0] < 15000:
                    his_dict['10K-15K'] += 1
                elif df.values[j][0] < 20000:
                    his_dict['15K-20K'] += 1
                else:
                    his_dict['20K以上'] += 1
        temp.append(i)
        for c in his_dict.values():
            temp.append(c)
        data.append(temp)

    return JsonResponse({'data': data})


def get_map_data(request):
    # 查询语句，选出employee表中的所有数据
    psql = 'select city from python;'
    jsql = 'select city from java;'
    wsql = 'select city from web;'
    uisql = 'select city from ui;'
    androidsql = 'select city from android;'
    mgsql = 'select city from meigong;'
    phpsql = 'select city from php;'
    sdxlsql ='select city from sdxl;'
    sfsql = 'select city from suanfagcs'

    # read_sql_query的两个参数: sql语句， 数据库连接
    pdf = pd.read_sql_query(psql, engine)
    jdf = pd.read_sql_query(jsql, engine)
    wdf = pd.read_sql_query(wsql, engine)
    uidf = pd.read_sql_query(uisql, engine)
    androiddf = pd.read_sql_query(androidsql, engine)
    mgdf = pd.read_sql_query(mgsql, engine)
    phpdf = pd.read_sql_query(phpsql, engine)
    sdxldf = pd.read_sql_query(sdxlsql, engine)
    sfdf = pd.read_sql_query(sfsql, engine)
    # print(df.values.T)
    # print(pd.value_counts(df.values.T[0]))
    # 读取数据库数据，得到DataFrame，将数据转换为前端页面需要的数据样式

    # 统计城市这一列数据中相同值出现的次数(在某个城市中当前python职位数)
    pres = pd.value_counts(pdf.values.T[0])
    # 统计城市这一列数据中相同值出现的次数(在某个城市中当前Java职位数)
    jres = pd.value_counts(jdf.values.T[0])
    wres = pd.value_counts(wdf.values.T[0])
    uires = pd.value_counts(uidf.values.T[0])
    androidres = pd.value_counts(androiddf.values.T[0])
    mgres = pd.value_counts(mgdf.values.T[0])
    phpres = pd.value_counts(phpdf.values.T[0])
    sdxlres = pd.value_counts(sdxldf.values.T[0])
    sfres = pd.value_counts(sfdf.values.T[0])
    data = []
    for i in range(len(pres)):
        temp = dict()
        temp['name'] = pres.index[i]
        for j in range(len(jres)):
            if jres.index[j] == pres.index[i]:
                temp['value'] = [int(pres[i]), int(jres[j])]
        for w in range(len(wres)):
            if wres.index[w] == pres.index[i]:
                temp['value'].append(int(wres[w]))
        for u in range(len(uires)):
            if uires.index[u] == pres.index[i]:
                temp['value'].append(int(wres[u]))
        for a in range(len(androidres)):
            if androidres.index[a] == pres.index[i]:
                temp['value'].append(int(wres[a]))
        for m in range(len(mgres)):
            if mgres.index[m] == pres.index[i]:
                temp['value'].append(int(wres[m]))
        for php in range(len(phpres)):
            if phpres.index[php] == pres.index[i]:
                temp['value'].append(int(wres[php]))
        for sdxl in range(len(sdxlres)):
            if sdxlres.index[sdxl] == pres.index[i]:
                temp['value'].append(int(wres[sdxl]))
        for sf in range(len(sfres)):
            if sfres.index[sf] == pres.index[i]:
                temp['value'].append(int(wres[sf]))
        data.append(temp)
    # print(data)
    # 返回json格式的响应给浏览器
    return JsonResponse({'data': data})
