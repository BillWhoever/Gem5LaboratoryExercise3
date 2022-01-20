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
runs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
	
for x in benchmarks:		#Benchmark loop
	for y in runs:		#Run loop (# of machine tested)
		os.system("python2 GEM5ToMcPAT.py -o ./McPatInput/{}{}.xml ./gem5Output/{}/{}/stats.txt ./gem5Output/{}/{}/config.json inorder_arm.xml".format(x, y, x, x, y) )	#executes the GEM5ToMcPAT.py with the desired I/O
print('process is completed')

