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

with open("dataOutput.txt", "a") as o:
	for y in runs:
		o.write("- Machine #{} -".format(y) )
		o.write("\n")
		for x in benchmarks:
			o.write("\n")
			o.write("- Benchmark: {} - CPI = ".format(x) )
			a_file = open("gem5Output/{}/{}/stats.txt".format(x, y))		#opens the correct stats.txt file
			lines_to_read = [28]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line = line [44 : 52]					#prints the IPC
					o.write(line)
			o.write("-")
			a_file = open("EnergyPrinterOutput/output{}{}.txt".format(x, y))	#opens the correct outputxx.txt file to write
			lines_to_read = [3]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					o.write(line)
			a_file = open("McPatOutput/results{}{}.txt".format(x, y))		#opens the correct resultsxx.txt file to read
			lines_to_read = [61, 66, 63, 65]					#print the Core data
			o.write ("- Core Data -")
			o.write("\n")
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					o.write(line)
			a_file = open("McPatOutput/results{}{}.txt".format(x, y))		#reopens the correct resultsxx.txt file to read
			o.write ("- L2 Data -")
			o.write("\n")
			lines_to_read = [277, 282, 279, 281]					#print the L2 data
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					o.write(line)
		o.write("\n")

	print('process is completed')

