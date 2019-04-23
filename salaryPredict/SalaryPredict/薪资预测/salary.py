from sklearn.preprocessing import LabelEncoder as LE
from sklearn.linear_model import LinearRegression as LR
import pandas as pd

data = pd.read_csv('./Python.csv', encoding="UTF-8")

# 将各字符分类变量重编码为数值分类变量
le = LE()

data['city'] = le.fit_transform(data['city'].values)  # 城市重编码

data['education'] = data['education'].replace('大专', 0)  # 学历重编码
data['education'] = data['education'].replace('本科', 1)
data['education'] = data['education'].replace('硕士', 2)
data['education'] = data['education'].replace('博士', 3)

# 去除NaN数据
data = data.fillna(method='ffill')

# 特征选择
X = data[['city', 'experience', 'education', 'skill']]
# 结果集
y = data['salary']

# 模型学习
model = LR()
model.fit(X, y)


# 构建预测函数
def wage_pred(area, exp, xueli, skill):
    area_index = list(le.classes_).index(area)
    xueli_index = list(('大专', '本科', '硕士', '博士')).index(xueli)
    wage_pred = model.predict([[area_index, exp, xueli_index, skill]])
    print('您的预测薪资为%.2f元/月' % wage_pred)
    return wage_pred


# 测试代码
if __name__ == '__main__':
    # city = str(input('请输入城市地区(北京、上海、广州、深圳、成都)：'))
    # exp = int(input('请输入工作经验(0-8)：'))
    # edu = str(input('请输入学历(大专、本科、硕士、博士)：'))
    # skill = int(input('请输入技能个数：'))
    # wage_pred(city, exp, edu, skill)
    pass
