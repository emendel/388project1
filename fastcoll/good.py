#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """


         x��&� w}�/!:�����I�M��8�*2�_���-g�#7w�l3BG%MM@��iXu"�D��.��|=^�Eg�����t�!՗��Ljy�7)ֹ(uc1Wu��^���Y��,������e9<W


"""
from hashlib import sha256
print sha256(blob).hexdigest()


