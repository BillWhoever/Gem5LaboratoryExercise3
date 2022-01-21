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
		os.system("echo --- RESULTS FOR Benchmark:{} and Run#:{} --- FINISHED!".format(x, y, x, y) )
		os.system("python2 print_energy.py ./McPatOutput/results{}{}.txt ./gem5Output/idealNewResults/{}/stats.txt > ./EnergyPrinterOutput/output{}{}.txt".format(x, y, x, x, y) )
print('process is completed')

