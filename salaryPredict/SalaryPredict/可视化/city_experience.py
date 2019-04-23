import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_csv('./Python.csv', encoding="UTF-8")

fig, ax = plt.subplots(1, 2, figsize=(18, 8))
education_Count = data.education.value_counts()
experience_Count = data.experience.value_counts()
patches, l_text, p_text = ax[0].pie(education_Count, autopct='%.2f%%', labels=education_Count.index)
m = -0.01
for t in l_text[6:]:
    t.set_y(m)
    m += 0.1
    print(t)
for p in p_text[6:]:
    p.set_y(m)
    m += 0.1
ax[0].set_title('Python招聘学历分布', fontsize=24)
index, bar_width = np.arange(len(experience_Count)), 0.6
ax[1].barh(index * (-1) + bar_width, experience_Count, tick_label=experience_Count.index, height=bar_width)
for x, y in enumerate(experience_Count):
    plt.text(y + 0.1, x * (-1) + bar_width, '%s' % y, va='center')
ax[1].set_title('Python招聘工作经验要求(单位:年)', fontsize=24)
# plt.savefig("5.jpg")
plt.show()

