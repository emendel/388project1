#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           *���t�u���Xc8��b9a }<(
:Zh�\����>vC�k&D�5n����<W-�r!�m([���8�%��.OTo�GC��t�KO�c��\�	o�^��%7��W�����J¶�c��
"""
from hashlib import sha256
if ((sha256(blob).hexdigest()) == "2f8b9f096276b7af2770125cda785e40ed4ece80ef7c9702f9c5eb3c4d7841ee"):
	print ("I come in peace.")
elif ((sha256(blob).hexdigest()) == "75653fad5aac031c9feffb076ccc8471fc1e7a160f76594d765e92a0171a335c"):
	print ("Prepare to be destroyed!")