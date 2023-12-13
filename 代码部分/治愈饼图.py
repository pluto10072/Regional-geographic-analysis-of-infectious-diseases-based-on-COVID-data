import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def pie_with_legend(data, label_column, value_column, title, colors=None, fontsize=12):
    """
    :param data: pandas.DataFrame，包含用于生成饼图的数据
    :param label_column: str，数据中用于显示标签的列名
    :param value_column: str，数据中用于显示数值的列名
    :param title: str，饼图标题
    :param colors: list，饼图颜色列表，默认为None
    :param fontsize: int，图表字体大小，默认为12
    :return: None
    """
    fig, ax = plt.subplots()

    # 获取饼图的数据和标签
    pie_data = data[value_column].values
    labels = data[label_column].values

    # 绘制饼图
    wedges, _, _ = ax.pie(pie_data, labels=None, colors=colors, autopct='%1.1f%%',
                          textprops={'fontsize': fontsize})
    ax.set_title(title, fontsize=fontsize)

    # 解决标签重叠问题
    bbox_props = dict(boxstyle="square", fc="w", ec="0.5", alpha=0.9)
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"), zorder=0, va="center",
              bbox=bbox_props)
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y), fontsize=fontsize,
                    horizontalalignment=horizontalalignment, **kw)

    plt.show()


# 中文显示设置
plt.rcParams['font.sans-serif'] = 'SimHei'

# 导入数据
cured2022 = pd.read_excel('cured2022.xlsx', index_col=0)
cured2021 = pd.read_excel('cured2021.xlsx', index_col=0)
cured2020 = pd.read_excel('cured2020.xlsx', index_col=0)

# 绘制饼图
pie_with_legend(cured2022, 'provinceName', 'countDifference', '2022年各省治愈人数占全国治愈人数的百分比', fontsize=14)
pie_with_legend(cured2021, 'provinceName', 'countDifference', '2021年各省治愈人数占全国治愈人数的百分比', fontsize=14)
pie_with_legend(cured2020, 'provinceName', 'countDifference', '2020年各省治愈人数占全国治愈人数的百分比', fontsize=14)

