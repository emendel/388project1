#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            
����_" ��9Le����wL�81��ӟ�&��R3X��93����[��,���\ ]3͵�1g9wڋY�D F+VE^���\����a}��q�]{��aK��g�Pf�M�4�̫%*M��
"""
from hashlib import sha256
print sha256(blob).hexdigest()