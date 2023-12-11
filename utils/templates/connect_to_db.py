#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 17:17
# @Author  : Berlin Wong
# @File    : connect_to_db.py
# @Software: PyCharm
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def get_engine():
    # 加载 .env 文件中的环境变量
    load_dotenv()

    # 获取 MySQL 配置信息
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_port = os.getenv("MYSQL_PORT")
    mysql_database = os.getenv("MYSQL_DATABASE")
    mysql_username = os.getenv("MYSQL_USERNAME")
    mysql_password = os.getenv("MYSQL_PASSWORD")

    # 构建 MySQL 连接字符串
    db_connection_str = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"

    # 创建 SQLAlchemy 引擎
    engine = create_engine(db_connection_str)

    return engine
