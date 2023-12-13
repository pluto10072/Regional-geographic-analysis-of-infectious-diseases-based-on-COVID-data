import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def pie_with_legend(data, label_column, value_column, title, colors=None, fontsize=12, threshold=0.02, alpha=0.9):
    """
    :param data: pandas.DataFrame，包含用于生成饼图的数据
    :param label_column: str，数据中用于显示标签的列名
    :param value_column: str，数据中用于显示数值的列名
    :param title: str，饼图标题
    :param colors: list，饼图颜色列表，默认为None
    :param fontsize: int，图表字体大小，默认为12
    :param threshold: float，标签显示阈值，低于该阈值的部分将不会显示，默认为0.02
    :param alpha: float，图例透明度，默认为0.9
    :return: None
    """
    fig, ax = plt.subplots()

    # 获取饼图的数据和标签
    pie_data = data[value_column].values
    labels = data[label_column].values

    # 计算百分比并过滤掉数量过低的部分
    total = sum(pie_data)
    percentages = [round(val / total * 100, 2) for val in pie_data]
    labels_to_show = []
    sizes_to_show = []
    colors_to_show = []
    for i in range(len(labels)):
        if percentages[i] < threshold:
            continue
        labels_to_show.append(labels[i])
        sizes_to_show.append(pie_data[i])
        if colors is not None:
            colors_to_show.append(colors[i])
    if colors is None:
        colors_to_show = None

    # 绘制饼图
    wedges, _, autopct = ax.pie(sizes_to_show, colors=colors_to_show, autopct='%1.1f%%',
                                     textprops={'fontsize': fontsize})
    ax.set_title(title, fontsize=fontsize)

    # 添加图例并设置透明度
    legend_labels = [f"{label}: {percentage:.2f}%" for label, percentage in zip(labels_to_show, percentages) if
                     percentage >= threshold]
    legend_patches = ax.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0.5), prop={'size': fontsize}).get_patches()
    for patch in legend_patches:
        patch.set_alpha(alpha)

    # 解决标签重叠问题
    bbox_props = dict(boxstyle="square", fc="w", ec="0.5", alpha=1)
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
plt.rcParams['font.sans-serif'] = 'simhei'

# 导入数据
comformed2022 = pd.read_excel('2022comformed.xlsx', index_col=0)
comformed2021 = pd.read_excel('2021comformed.xlsx', index_col=0)
comformed2020 = pd.read_excel('2020comformed.xlsx', index_col=0)
comform2022 = pd.read_excel('2022comform.xlsx', index_col=0)
comform2021 = pd.read_excel('2021comform.xlsx', index_col=0)
comform2020 = pd.read_excel("2020comform.xlsx", index_col=0)
comform2020_1 = pd.read_excel("2020comform1.xlsx", index_col=0)

# 绘制饼图
pie_with_legend(comform2022, 'provinceName', 'countDifference', '2022年各省确诊人数占全国确诊人数的百分比', threshold=0, alpha=1)
pie_with_legend(comform2021, 'provinceName', 'countDifference', '2021年各省确诊人数占全国确诊人数的百分比', threshold=0, alpha=1)
pie_with_legend(comform2020, 'provinceName', 'countDifference', '2020年各省确诊人数占全国确诊人数的百分比', threshold=0, alpha=1)

pie_with_legend(comformed2022, 'provinceName', 'countDifference', '2022年各省确诊人数占全国确诊人数的百分比\n（除台湾、香港）', threshold=0, alpha=1)
pie_with_legend(comformed2021, 'provinceName', 'countDifference', '2021年各省确诊人数占全国确诊人数的百分比\n（除台湾、香港）', threshold=0, alpha=1)
pie_with_legend(comformed2020, 'provinceName', 'countDifference', '2020年各省确诊人数占全国确诊人数的百分比\n（除台湾、香港）', threshold=0, alpha=1)

pie_with_legend(comform2020_1, 'provinceName', 'countDifference', '2020年各省确诊人数占全国确诊人数的百分比\n（除台湾、香港、湖北）', threshold=0, alpha=1)
