import pandas as pd
from pyecharts import Pie, configure
from pyecharts import Bar, WordCloud

# 设置全局主题
configure(global_theme='dark')

# 读取数据
data = pd.read_csv('./Python3.csv', encoding="UTF-8")

# 统计字段数量
city_count = data.city.value_counts()
experience_count = data.experience.value_counts()
education_count = data.education.value_counts()
skill = data.skill.value_counts()

# 统计薪资平均值
Salary_Education = data.groupby('experience', as_index=False)['salary'].mean()
Salary_Education['Salary'] = Salary_Education.salary
Salary_Education = Salary_Education.sort_values('Salary', ascending=True)

# 设置条形图X,Y坐标
# attr = Salary_Education.experience
# value = Salary_Education.Salary
attr = experience_count.index
value = experience_count
# 设置条形图标题
bar = Bar('Python招聘经验统计')

# 条形图通用配置
bar.add('经验', attr, value, is_more_utils=True)

# 导出HTML页面
# bar.render()

# 饼图配置
pie = Pie('Python招聘经验比例', title_pos='center')
attr = experience_count.index
value = experience_count
pie.add('经验', attr, value, is_label_show=True, radius=[30, 75], is_legend_show=False)
# pie.render()

# 词云图绘制
myWordCloud = WordCloud("Python技能需求分析", width=1000, height=600, title_pos='center')
name = ['redis', 'mysql', 'mongodb', 'django', 'flask', 'tordano', 'scrapy', 'linux', 'centos', 'shell', 'unix',
        'spark', 'hadoop', 'html', 'css', 'js', 'ajax', 'sqlserver', 'hbase', 'ansible', 'sklearn', 'pandas', 'numpy',
        'tensorflow', 'selenium', 'tcp', 'ip', 'http', 'https', 'nginx', 'xpath', 'git', 'memcached',
        'matplotlib', 'webpack', 'socket', 'python']
value = [1000, 800, 600, 500, 300, 1500, 2000, 2100, 2500,
         700, 600, 1000, 800, 600, 500, 300, 1500, 2000, 2100,
         2500, 700, 600, 1000, 800, 600, 500, 300, 1500, 2000,
         2100, 2500, 700, 600, 1000, 800, 600, 4000]
myWordCloud.add("", name, value, word_size_range=[20, 100])
myWordCloud.render()
