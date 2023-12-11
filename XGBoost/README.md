![Logo](https://raw.githubusercontent.com/dmlc/dmlc.github.io/master/img/logo-m/xgboost.png)

> XGBoost是一个优化的分布式梯度增强库，旨在实现高效，灵活和便携。

## 安装

python库文件安装: `pip install xgboost`

## 简介

XGBoost，Extreme Gradient Boosting。其基于梯度提升决策树 gradient boosted tree（GBDT/GBRT/GBM）。

主要应用于监督学习中，是数据比赛中常用的大杀器。

CART，分类与回归树 Classification and Regression Tree，从名字就可以看出既可以处理分类也可以处理回归问题。CART能够通过对变量进行划分来不断分裂生成一个二叉树，首先对一维数据排序，然后对排序的特征进行切分，最终的切分点由评估指标确定，分类指标为基尼指数，回归指标是最小平方和，找到切分点后生成左右子树。
