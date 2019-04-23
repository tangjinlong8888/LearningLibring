import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_csv('./Python.csv', encoding="UTF-8")

Salary_Education = data.groupby('city', as_index=False)['salary'].mean()
Salary_Education['Salary'] = Salary_Education.salary
Salary_Education = Salary_Education.sort_values('Salary', ascending=True)
plt.bar(Salary_Education.city, Salary_Education.Salary, width=0.6)
for x, y in enumerate(Salary_Education.salary):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.title('各城市对应的平均工资水平(单位:元/月)', fontsize=20)
plt.savefig("4.jpg")
plt.show()
