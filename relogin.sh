#!/bin/bash
FULLPATH="$PWD/$(dirname $0)"
cd $FULLPATH
python3 logout.py
python3 login.py
