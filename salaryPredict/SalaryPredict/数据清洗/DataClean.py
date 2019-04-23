import re
import pandas as pd

# 数据去重

data = pd.read_json('Python2.json', encoding='UTF-8')
data = data.drop_duplicates()
data.to_csv('Python4.csv', index=False,
            columns=["title", "salary", "experience", "education", "skill", "city"])

data = pd.read_csv('./Python4.csv', encoding="UTF-8")


# 数据处理

# 城市字符串处理函数
def get_area(area):
    if '-' in area:
        area = area.split('-')
        return area[0]
    else:
        return area


# 经验字符串处理函数
def get_exp(exp):
    # 1年经验，2年经验，3-9年经验，无工作经验
    if '-' in exp:
        exp = exp.split('-')
        return exp[0]
    elif exp == '无工作经验':
        return 0
    else:
        return exp[0]


# 工资字符串处理函数
def get_wage(wage):
    # 三种情况举例：1.5-2千/月,0.4-1.2万/月,12-35万/年

    if wage.endswith('千/月'):
        wage = wage.replace('千/月', '')
        wage = wage.split('-')
        wage = ((float(wage[0]) + float(wage[1])) * 1000 / 2)
        return int(wage)
    elif wage.endswith('万/月'):
        wage = wage.replace('万/月', '')
        wage = wage.split('-')
        wage = ((float(wage[0]) + float(wage[1])) * 10000 / 2)
        return int(wage)
    elif wage.endswith('万/年'):
        wage = wage.replace('万/年', '')
        wage = wage.split('-')
        wage = ((float(wage[0]) + float(wage[1])) * 10000 / (2 * 12))
        return int(wage)
    elif wage.endswith('元/天'):
        wage = wage.split('元/天')
        wage = ((float(wage[0])) * 30)
        return int(wage)


# 技能去重 转换小写 计数
def get_lower(skill):
    skill = str(skill).lower()
    skill = str([x for x in skill if skill.count(x) == 1])
    result = re.findall(r"[^a-zA-Z]+", skill)
    return len(result)


# 将上述各处理函数应用到对应列
data["city"] = data["city"].apply(get_area)
data["experience"] = data["experience"].apply(get_exp)
data["salary"] = data["salary"].apply(get_wage)
data["skill"] = data["skill"].apply(get_lower)
data.to_csv('Python5.csv', index=False,
            columns=["title", "salary", "experience", "education", "skill", "city"])
# print(data.head(2))
