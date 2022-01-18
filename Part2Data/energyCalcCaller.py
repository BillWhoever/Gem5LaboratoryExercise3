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
runs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
	
for x in benchmarks:
	for y in runs:
		os.system("echo --- RESULTS FOR Benchmark:{} and Run#:{} --- FINISHED!".format(x, y, x, y) )
		os.system("python2 print_energy.py ./McPatOutput/results{}{}.txt ./gem5Output/{}/{}/stats.txt > ./Output/output{}{}.txt".format(x, y, x, y, x, y) )
print('process is completed')

