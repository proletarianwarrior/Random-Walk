# -*- coding: utf-8 -*-
# @Time : 2022/6/13 18:46
# @Author : DanYang
# @File : Machine_Learning_Predicts_Major_Percentage.py
# @Software : PyCharm
from plotly.graph_objs import Bar, Layout, Scatter
from plotly import offline

"""
设置分流数据类
"""


class MachineTriageData:
    def __init__(self):
        # 数据初始化
        self.professional_directory = {135: '测控技术与仪器(食品方向)', 103: '测控技术与仪器',
                                       105: '车辆工程', 136: '机械工程(3D打印国际班)', 122: '机械工程', 102: '工业设计',
                                       201: '材料科学与工程', 367: '能源与动力工程(热流国际)',
                                       337: '能源动力工程', 309: '环境工程', 302: '核工程与核技术', 310: '新能源科学与工程',
                                       1720: '工程力学', 1704: '飞行器设计与工程', 703: '建筑学', 732: '人居环境科学与技术',
                                       721: '建筑环境与能源应用工程', 702: '土木工程', 722: '环境科学',
                                       1502: '化学工程与工艺', 1501: '过程装备与控制工程'}
        self.planned_number_of_recruits = [30, 29, 29, 23, 207, 24, 123, 20, 252, 30,
                                           97, 32, 90, 29, 44, 15, 20, 22, 14, 51, 54]
        self.admissions = [33, 20, 28, 23, 181, 23, 115, 18, 219, 30, 94, 32, 81, 29,
                           40, 8, 18, 15, 20, 53, 52]
        self.max_scores = {84.53: 260, 84.22: 285, 83.76: 337, 90.03: 7, 87.79: 66,
                           86.94: 108, 89.2: 108, 91.53: 2, 89.45: 18, 83.69: 350,
                           88.94: 29, 88.92: 30, 88.62: 37, 85.39: 200, 88.34: 47,
                           73.99: 1028, 82.63: 436, 83.75: 338, 86.22: 138, 89.79: 10,
                           82.88: 411}
        self.min_scores = {66.78: 1168, 77.25: 895, 74.41: 1012, 84.81: 238, 51.22: 1230,
                           75.82: 957, 40.65: 1235, 86.7: 112, 72.07: 1092, 55.4: 1222,
                           62.4: 1197, 80.14: 662, 58.61: 1210, 71.55: 1106, 43.51: 1233,
                           54.82: 1288, 58.04: 1216, 14.7: 1240, 33.15: 1237, 43.8: 1234,
                           65.37: 1179}
        self.means_scores = [74.18, 80.85, 79.38, 88.39, 81.76, 81.55, 77.3, 88.55, 82.49,
                             74.88, 78.5, 85.15, 78.17, 79.41, 69.56, 63.73, 68.75, 64.05,
                             64.89, 68.59, 74.61]


"""
数据可视化
"""
admission_result = MachineTriageData()
width = 1
width1 = 0.2
trace1 = Bar(
    x=list(admission_result.professional_directory.values()),
    y=admission_result.planned_number_of_recruits,
    name='计划招生',
    width=width1,
    marker=dict(
        color='#1C86EE',
        line=dict(
            color='#104E8B',
            width=width)
    )

)
trace2 = Bar(
    x=list(admission_result.professional_directory.values()),
    y=admission_result.admissions,
    name='实际录取',
    width=width1,
    marker=dict(
        color='#1874CD',
        line=dict(
            color='#104E8B',
            width=width)
    )
)
trace3 = Bar(
    x=list(admission_result.professional_directory.values()),
    y=list(admission_result.max_scores.keys()),
    name='最高成绩',
    width=width1,
    marker=dict(
        color='#00FF00',
        line=dict(
            color='#008B45',
            width=width)
    ),
    text=list(admission_result.max_scores.values()),
    textposition='outside',
    textfont={'color': 'black', 'size': 10}
)
trace4 = Bar(
    x=list(admission_result.professional_directory.values()),
    y=list(admission_result.min_scores.keys()),
    name='最低成绩',
    width=width1,
    marker=dict(
        color='#008B00',
        line=dict(
            color='#008B45',
            width=width)
    ),
    text=list(admission_result.min_scores.values()),
    textposition='outside',
    textfont={'color': 'black', 'size': 10}
)
trace5 = Scatter(
    x=list(admission_result.professional_directory.values()),
    y=admission_result.means_scores,
    name='平均分',
    mode="markers+lines+text",
    text=admission_result.means_scores,
    textposition='top left',
    textfont={'color': 'red', 'size': 10}
)

data = [trace1, trace2, trace3, trace4, trace5]
my_layout = Layout(
    title='西安交通大学19级分流数据',
    xaxis={'title': '专业名称'},
    yaxis={'title': '人数/分数'}
)
# 在py文件目录中生成html文件，便于离线观看
offline.plot({'data': data, 'layout': my_layout}, filename='xjtu_triage_data.html')
