#!/usr/bin/python
from optparse import OptionParser
import os
import sys
import re
import json
import types
import math
from xml.etree import ElementTree as ET

benchmarks = ["401bzip2", "429mcf", "456hmmer", "458sjeng", "470lbm"]
runs = ["idealNew"]
	
for x in benchmarks:
	for y in runs:
		os.system("python2 GEM5ToMcPAT.py -o ./McPatInput/{}{}.xml ./gem5Output/idealNewResults/{}/stats.txt ./gem5Output/idealNewResults/{}/config.json inorder_arm.xml".format(x, y, x, x) )
print('process is completed')

