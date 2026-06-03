#!/usr/bin/env python3

import os

dir = "files"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, dir)
os.mkdir(path)

for i in range(1, 51):
	open(f"files/{i:02d}_WSC.txt", "w")
