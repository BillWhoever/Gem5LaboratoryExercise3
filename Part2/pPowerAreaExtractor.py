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

with open("dataOutputB.txt", "a") as o:							#opens the dataOutputB.txt file to write
	for y in runs:
		o.write("Machine #{}".format(y) )
		o.write("\n")
		for x in benchmarks:
			o.write("Benchmark:-{}- CPI:-".format(x) )
			a_file = open("gem5Output/{}/{}/stats.txt".format(x, y))	#opens the correct stats.txt file to read
			lines_to_read = [28]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line = line [44 : 52]
					o.write(line)					#prints the IPC
			a_file = open("McPatOutput/results{}{}.txt".format(x, y))	#opens the correct resultsxx.txt file to read
			lines_to_read = [15]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line = line [14 : -1]				
					o.write("- PeakPower:-{}".format(line) )	#print Peak Power
			a_file = open("McPatOutput/results{}{}.txt".format(x, y))	#opens the correct resultsxx.txt file to read
			lines_to_read = [14]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line = line [8 : -1]				
					o.write("-Area:-{}".format(line) )		#print Area
			o.write("\n")
	print('process is completed')
