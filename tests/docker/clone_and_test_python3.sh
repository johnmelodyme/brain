#!/usr/bin/env bash

# install dev version
git clone https://github.com/brain-ai/brain.git brain;
cd brain;
git checkout master;

# install
sudo python3 setup.py install
git clone https://github.com/brain-ai/assistant
cd assistant

# tests
export LANG=C.UTF-8
python3 -m unittest discover
