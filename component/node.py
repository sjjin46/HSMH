#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
作者: sjjin
邮件: sj_jin@vip.hnist.edu.cn
日期: 2022年12月20日
说明: 重要的组件类
"""

from enum import Enum
from config.config import MAX_NUM_QUEUE,MAX_NUM_PORT

class NodeType(Enum):
    sw = 0
    es = 1

class Node(int):
    def __init__(self, id: int, type: NodeType) -> None:
        self.id = id
        self.type = type
        self.num_port = MAX_NUM_QUEUE
        self.num_queue = MAX_NUM_PORT


