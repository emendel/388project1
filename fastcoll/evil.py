#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """


         x��&� w}�/!:������I�M��8�*2�_���-g�#�7w�l3BG%MM@���Xu"�D��.��|=^�Eg���K�t�!՗��Ljy�7)ֹ(uc1Wu��^b��Y��,�������9<W


"""
from hashlib import sha256
print sha256(blob).hexdigest()


