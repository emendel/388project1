#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �T�Y>D����I�>-�~��O���[�9�˯B�d����!�yoH<�6o9�YL -�]@|�hN�N++��X�:�$�L�n��`���)� x`h��{2h�Ư���a��W����B�уH�,s,�
"""
from hashlib import sha256
print sha256(blob).hexdigest()