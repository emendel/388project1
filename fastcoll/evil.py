#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """


          ��:����S�s&d"M��Ԯ0�[���$����|�����؁RIXb��N���);2M){��Z`ۘ�SH�3�_�Mq��&1�Z���F�ΜFYP � m� 1e�O���9�35C[7�)�"


"""
from hashlib import sha256
print sha256(blob).hexdigest()