#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 11:10
# @Author  : Berlin Wong
# @File    : mian.py
# @Software: PyCharm

# 导入必要的库
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import xgboost as xgb

# 读取股市数据
# 假设数据文件为CSV格式，包含特征和标签列
column_names = ['Code', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Amount', 'AdjustFlag']

data = pd.read_csv('../../data/history__stock_k_data_2022_by_day.csv', header=None, names=column_names)

# 将Date列转换为日期时间格式
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# 选择指定日期范围的数据
start_date = '20220101'
end_date = '20220531'
selected_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# 特征选择
# 请根据实际情况选择合适的特征列
features = ['feature1', 'feature2', 'feature3']
X = data[features]

# 标签选择
# 请根据实际情况选择合适的标签列
y = data['label']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建XGBoost模型
model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型性能
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 特征重要性分析
xgb.plot_importance(model)

# 在实际应用中，你可能需要保存模型以便后续使用
# model.save_model('stock_model.json')
