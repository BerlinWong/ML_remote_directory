#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 15:20
# @Author  : Berlin Wong
# @File    : sortByDayAndTakeTheMonth.py
# @Software: PyCharm
import pandas as pd

# 读取CSV文件并为首行添加列名
column_names = ['code', 'date', 'time', 'open', 'high', 'low', 'close', 'volume', 'amount', 'adjustflag']
data = pd.read_csv('../../data/history__stock_k_data_2022.csv', header=None, names=column_names)

# 将date和time列转换为字符串类型
data['date'] = data['date'].astype(str)
data['time'] = data['time'].astype(str).str[:-3]
data['time'] = pd.to_datetime(data['time'], format='%Y%m%d%H%M%S')
print(data.head())

# 按日期和时间排序
sorted_data = data.sort_values(by=['date', 'time'])

# 导出为新的CSV文件
sorted_data.to_csv('../../data/history__stock_k_data_2022_by_day.csv', index=False)

# 显示排序后的数据
print(sorted_data.head())
