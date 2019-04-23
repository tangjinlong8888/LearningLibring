import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from imageio import imread

# 设置背景样式
back_image = imread('python-logo.jpg')

# 读取数据
data = open('Python3.csv', encoding='UTF-8').read()

# 使用jieba分词
word_list = jieba.cut(data, cut_all=True)
wl_space_split = " ".join(word_list)

# 配置词云图样式
word_cloud = WordCloud(font_path='simhei.ttf',
                       background_color="#333333",
                       mask=back_image,
                       random_state=3,
                       ).generate(wl_space_split)

# 配置图片尺寸 分辨率 字体
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 500
plt.rcParams['figure.dpi'] = 500

# 绘制图片
plt.imshow(word_cloud)

# 不显示坐标轴
plt.axis("off")

# 储存图片
plt.savefig("wordcloud4.jpg", dpi=500)

# 展示图片
plt.show()
