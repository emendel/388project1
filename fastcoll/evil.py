#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �V���3e��ҳ�Bd�_���W:��C��ʄ��ެ�G\A��#�e��ӱ�7���esI�Ƭp��ŧ"�m���*��6�Z�w��X]�}I��7R��L�ϋ�]���АVmp���J"""
from hashlib import sha256
print sha256(blob).hexdigest()