#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���N�A�I�����O��h��04L�9��+�����f�k�s�e���bo�u��a@[:b@	�x���R˭�r4�Q�F֦y"$~�Y�[���].=!��7؂�h�ύh��>`9�4ϔ����u
"""
from hashlib import sha256
print sha256(blob).hexdigest()