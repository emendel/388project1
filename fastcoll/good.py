#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """

          ��:����S�s&d"M��Ԯ��[���$����|������RIXb��N���)�2M){��Z`ۘ�SH�3�_�Mqr�&1�Z���F�ΜFYP � m� �e�O���9�35C[7J)�"

"""
from hashlib import sha256
print sha256(blob).hexdigest()