#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �V���3e��ҳ�Bd�_�U�W:��C��ʄ��ެ�G\A�ԣ�e��ӱ�7���es��Ƭp��ŧ"�m���*���6�Z�w��X]�}I��7R��L�ϋ9^���АVmpb��J
"""
from hashlib import sha256
print sha256(blob).hexdigest()