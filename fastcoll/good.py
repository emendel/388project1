#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �T�Y>D����I�>-�~�=O���[�9�˯B�d����!�yoH<D6o9�YL -�]@|i�hN�N++��X�:�$�L�n�[`���)� x`h��{2h�Ư���a�W����B�уHʬs,�
"""
from hashlib import sha256
print sha256(blob).hexdigest()